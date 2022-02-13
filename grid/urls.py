from django.urls import path
from .views import index, get_visit

urlpatterns = [
    path('', index, name='index'),
    path('visit/<str:slug>', get_visit, name='visit'),
]
