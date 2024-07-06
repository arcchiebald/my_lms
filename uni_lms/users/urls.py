from django.urls import path
from . import views


app_name = "users"

urlpatterns = [
    path('', views.login_view, name='login'),
    path('test/', views.test_view, name='test'),
]