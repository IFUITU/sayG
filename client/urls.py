from django.urls import path
from .views import signup, SignInOutView

app_name = 'client'
urlpatterns = [
    path("signup/", signup, name="signup"),
    path("log/", SignInOutView.as_view(), name="log"),    
]