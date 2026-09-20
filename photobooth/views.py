from rest_framework import generics
from .models import PhotoSession
from .serializers import PhotoSessionSerializer

class PhotoSessionCreateView(generics.CreateAPIView):
    """
    Handles POST requests from the Capture Page.
    Accepts photo_1, photo_2, photo_3, and photo_4.
    """
    queryset = PhotoSession.objects.all()
    serializer_class = PhotoSessionSerializer

class PhotoSessionDetailView(generics.RetrieveAPIView):
    """
    Handles GET requests from the Review and Result Pages.
    Retrieves the session using its UUID to display photos, composite frames, and the QR code.
    """
    queryset = PhotoSession.objects.all()
    serializer_class = PhotoSessionSerializer
