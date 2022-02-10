from django.shortcuts import render, redirect
from django.views.generic import DetailView
from .models import Employee, Visits
from datetime import date


def index(request):
    employees = Employee.objects.all()
    visit = Visits.objects.filter(date=date.today())
    return render(request, "show.html", {'employees': employees, 'visits': visit})


def GetVisit(request, slug):
    visit = Visits.objects.filter(user__slug=slug)
    user = Employee.objects.get(slug=slug)
    return render(request, 'get_visits.html', {'visits': visit, 'user': user})
