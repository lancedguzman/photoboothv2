from django.urls import path
from . import views  # Import the local views.py file

urlpatterns = [
    # Endpoint for the Capture Page to upload the 4 photos
    path('sessions/create/', views.PhotoSessionCreateView.as_view(), name='session-create'),
    
    # Endpoint for Review and Result Pages to retrieve session data via UUID
    path('sessions/<uuid:pk>/', views.PhotoSessionDetailView.as_view(), name='session-detail'),

    # Download endpoint mapped to your local download_composite function
    path('download/<uuid:pk>/', views.download_composite, name='session-download'),
]
