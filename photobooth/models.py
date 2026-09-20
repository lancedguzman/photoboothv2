import uuid
from django.db import models
from .functions import generate_session_qr_code

class PhotoSession(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    photo_1 = models.ImageField(upload_to='photobooth/raw_photos/')
    photo_2 = models.ImageField(upload_to='photobooth/raw_photos/')
    photo_3 = models.ImageField(upload_to='photobooth/raw_photos/')
    photo_4 = models.ImageField(upload_to='photobooth/raw_photos/')
    
    composite_frame = models.ImageField(upload_to='photobooth/frames/', null=True, blank=True)
    gif_video = models.FileField(upload_to='photobooth/gifs/', null=True, blank=True)
    
    qr_code = models.ImageField(upload_to='photobooth/qrcodes/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Photobooth Session - {self.id}"

    def save(self, *args, **kwargs):
        # Trigger the external function if the QR code hasn't been generated yet
        if not self.qr_code:
            generate_session_qr_code(self)
            
        super().save(*args, **kwargs)
