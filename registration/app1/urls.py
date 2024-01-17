from django.urls import path
from .views import profile_view

urlpatterns = [
    # Other patterns...
    path('/', profile_view, name='profile'),
]