from django.urls import path
from .views import index, get_visit, export_excel
<<<<<<< HEAD
=======

>>>>>>> 4de1b879939bf1b159ad2351e0972c0e6babc0f9
urlpatterns = [
    path('', index, name='index'),
    path('visit/<str:slug>', get_visit, name='visit'),
    path('export/excel/', export_excel, name='export_excel'),
]

