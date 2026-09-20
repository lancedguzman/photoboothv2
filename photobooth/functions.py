import qrcode
from io import BytesIO
from django.core.files import File
from django.conf import settings

def generate_session_qr_code(session_instance):
    """
    Generates a QR code pointing to the session's download URL 
    and attaches it to the model instance.
    """
    base_url = getattr(settings, 'BASE_URL', 'http://127.0.0.1:8000')
    download_url = f"{base_url}/download/{session_instance.id}/"
    
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
