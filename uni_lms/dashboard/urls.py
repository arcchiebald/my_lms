from django.urls import path
from . import views


app_name = "dashboard"

urlpatterns = [
    path("", views.mainpage_view, name="mainpage"),
    path("logout/", views.logout_view, name="logout"),
]