from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404
from rest_framework import generics
from .models import PhotoSession
from .serializers import PhotoSessionSerializer
from .functions import generate_composite_frame

class PhotoSessionCreateView(generics.CreateAPIView):
    """
    Handles POST requests from the Capture Page.
    Accepts photo_1, photo_2, photo_3, and photo_4.
    """
    queryset = PhotoSession.objects.all()
    serializer_class = PhotoSessionSerializer

    def perform_create(self, serializer):
        # Save the instance first so the raw photo files are written to disk
        session = serializer.save()
        
        # Trigger the composite stitching (QR code is already handled in models.py save())
        generate_composite_frame(session)
        
        # Save the instance again to commit the new composite_frame file
        session.save()

class PhotoSessionDetailView(generics.RetrieveAPIView):
    """
    Handles GET requests from the Review and Result Pages.
    Retrieves the session using its UUID to display photos, composite frames, and the QR code.
    """
    queryset = PhotoSession.objects.all()
    serializer_class = PhotoSessionSerializer


def download_composite(request, pk):
    """
    Serves the composite frame as a downloadable attachment.
    """
    session = get_object_or_404(PhotoSession, pk=pk)
    
    if not session.composite_frame:
        raise Http404("Photo is still processing or does not exist.")
        
    # Open the file and set headers to force a file download
    response = HttpResponse(session.composite_frame.read(), content_type="image/jpeg")
    response['Content-Disposition'] = f'attachment; filename="gdg_photobooth_{session.id}.jpg"'
    return response
