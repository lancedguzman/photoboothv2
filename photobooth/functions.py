import os
import qrcode
from io import BytesIO
from PIL import Image
from django.core.files import File
from django.conf import settings

def generate_session_qr_code(session_instance):
    """
    Generates a QR code pointing to the session's download URL 
    and attaches it to the model instance.
    """
    base_url = getattr(settings, 'BASE_URL', 'http://127.0.0.1:8000')
    download_url = f"{base_url}/api/download/{session_instance.id}/"
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(download_url)
    qr.make(fit=True)
    
    qr_img = qr.make_image(fill_color="black", back_color="white")
    
    canvas = BytesIO()
    qr_img.save(canvas, format='PNG')
    
    file_name = f'qr_{session_instance.id}.png'
    
    # Save the file to the instance's qr_code field without triggering a database save yet
    session_instance.qr_code.save(file_name, File(canvas), save=False)
    canvas.close()


def generate_composite_frame(session_instance):
    """
    Stitches the 4 raw photos onto the ga-2026-frame.png.
    """
    frame_path = os.path.join(settings.MEDIA_ROOT, 'frame', 'ga-2026-frame.png')
    
    if not os.path.exists(frame_path):
        print("Frame image not found at:", frame_path)
        return

    # Open the background frame
    frame = Image.open(frame_path).convert("RGBA")
    
    # Define bounding boxes (Left, Top, Right, Bottom) for the 4 slots.
    # Note: You will need to adjust these exact pixel coordinates to perfectly match ga-2026-frame.png.
    # Based on the visual layout, Photo 1 is large (top-left), Photos 2-4 are smaller (bottom row).
    boxes = [
        (180, 90, 840, 580),    # Slot 1 (Large top-left)
        (180, 640, 640, 980),   # Slot 2 (Bottom-left)
        (730, 640, 1190, 980),  # Slot 3 (Bottom-center)
        (1280, 640, 1740, 980), # Slot 4 (Bottom-right)
    ]
    
    photos = [session_instance.photo_1, session_instance.photo_2, session_instance.photo_3, session_instance.photo_4]
    
    for idx, photo_field in enumerate(photos):
        if photo_field and idx < len(boxes):
            box = boxes[idx]
            target_width = box[2] - box[0]
            target_height = box[3] - box[1]
            
            # Open, resize, and paste the captured photo
            img = Image.open(photo_field.path).convert("RGBA")
            img = img.resize((target_width, target_height))
            frame.paste(img, (box[0], box[1]))
            
    # Save the composite frame to memory, then attach to the model field
    canvas = BytesIO()
    frame.convert("RGB").save(canvas, format='JPEG', quality=90)
    
    file_name = f'composite_{session_instance.id}.jpg'
    session_instance.composite_frame.save(file_name, File(canvas), save=False)
    canvas.close()
