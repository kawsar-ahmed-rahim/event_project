from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.user_login,name = "user_login"),
    path('logout/',views.user_logout,name = "user_logout")
]
