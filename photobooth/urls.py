from django.urls import path
from .views import PhotoSessionCreateView, PhotoSessionDetailView

urlpatterns = [
    # Endpoint for the Capture Page to upload the 4 photos
    path('api/sessions/create/', PhotoSessionCreateView.as_view(), name='session-create'),
    
    # Endpoint for Review and Result Pages to retrieve session data via UUID
    path('api/sessions/<uuid:pk>/', PhotoSessionDetailView.as_view(), name='session-detail'),
]
