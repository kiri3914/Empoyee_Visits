from django.shortcuts import render, redirect
from datetime import date as d
from .models import Employee, Visits
from django.http import HttpResponse
import xlwt


def index(request):
    day = d.today()
    employees = Employee.objects.all()
    visit = Visits.objects.filter(date=day)
    if request.method == 'POST':
        day = request.POST['day']
        visit = Visits.objects.filter(date=day)
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


def export_excel(request):
    response = HttpResponse(content_type='applications/mc-excel')
    response['Content-Disposition'] = 'attachment; filename="visits.xls"'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet(f'{d.today()}.excel')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['date', 'user', 'visited', 'time_start', 'time_end', 'reason']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    font_style = xlwt.XFStyle()
    rows = Visits.objects.all().values_list('date', 'user__name', 'visited', 'time_start', 'time_end', 'reason')

    print('rows', rows)

    for row in rows:
        row_num += 1

        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)
    wb.save(response)

    return response


