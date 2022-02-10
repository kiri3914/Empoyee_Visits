from django.urls import path
from .views import index, GetVisit

urlpatterns = [
    path('', index, name='index'),
    path('visit/<str:slug>', GetVisit, name='visit')
]
