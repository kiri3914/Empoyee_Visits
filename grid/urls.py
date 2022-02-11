from django.urls import path
from .views import index, get_visit, export_excel
urlpatterns = [
    path('', index, name='index'),
    path('visit/<str:slug>', get_visit, name='visit'),
    path('export/excel/', export_excel, name='export_excel'),
]

