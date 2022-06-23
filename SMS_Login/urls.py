from django.contrib import admin
from django.urls import path
from otp_App.views import UserRegister
from otp_App import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', UserRegister.as_view(), name='register'),
    # path('varify/', VarifyOTP.as_view(), name='varify'),
    path('varify/', views.login, name='varify'),

]
