from django.shortcuts import render, redirect
from django.views.generic import DetailView
from datetime import date as d

from .models import Employee, Visits, Date
from .forms import DateForm


def index(request):
    day = d.today()
    employees = Employee.objects.all()
    visit = Visits.objects.filter(date__day=day)
    if request.method == 'POST':
        day = request.POST['day']
        visit = Visits.objects.filter(date__day=day)
    context = {
        'employees': employees,
        'visits': visit,
        'day': day
    }
    return render(request, "show.html", context)


def get_visit(request, slug):
    visit = Visits.objects.filter(user__slug=slug)
    user = Employee.objects.get(slug=slug)
    return render(request, 'get_visits.html', {'visits': visit, 'user': user})
