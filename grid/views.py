from django.shortcuts import render, redirect
from django.views.generic import DetailView
from datetime import date

from .models import Employee, Visits
from .forms import DateForm



def index(request):
    employees = Employee.objects.all()

    visit = Visits.objects.filter(date=date.today())
    if request.method == 'POST':
        form = DateForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form = DateForm()
    return render(request, "show.html", {'employees': employees, 'visits': visit,'form': form})


def GetVisit(request, slug):
    visit = Visits.objects.filter(user__slug=slug)
    user = Employee.objects.get(slug=slug)
    return render(request, 'get_visits.html', {'visits': visit, 'user': user})
