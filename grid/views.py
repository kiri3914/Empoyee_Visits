from django.shortcuts import render, redirect
from django.views.generic import DetailView
from .models import Employee, Visits
from datetime import date
from django.http import HttpResponse
import xlwt


def index(request):
    employees = Employee.objects.all()
    visit = Visits.objects.filter(date=date.today())
    return render(request, "show.html", {'employees': employees, 'visits': visit})


def get_visit(request, slug):
    visit = Visits.objects.filter(user__slug=slug)
    user = Employee.objects.get(slug=slug)
    return render(request, 'get_visits.html', {'visits': visit, 'user': user})


# def export_users_csv(request):
#     response = HttpResponse(content_type='text/csv')
#     response['Content-Disposition'] = 'attachment; filename="visits.csv"'
#
#     writer = csv.writer(response)
#     writer.writerow(['date', 'user', 'visited', 'time_start', 'time_end', 'reason'])
#
#     visits = Visits.objects.all()
#
#     for visit in visits:
#         writer.writerow([visit.date, visit.user, visit.visited, visit.time_start, visit.time_end, visit.reason])
#
#     return response


def export_excel(request):
    response = HttpResponse(content_type='applications/mc-excel')
    response['Content-Disposition'] = 'attachment; filename="visits.xls"'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('visits.excel')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['date', 'user', 'visited', 'time_start', 'time_end', 'reason']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    font_style = xlwt.XFStyle()
    rows = Visits.objects.all().values_list('date', 'user', 'visited', 'time_start', 'time_end', 'reason')

    for row in rows:
        row_num += 1

        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)
    wb.save(response)

    return response


