from django.http import HttpResponse
from django.shortcuts import render, redirect
from datetime import date as d
import xlwt

from .models import Employee, Visits
<<<<<<< HEAD
from datetime import date
from django.http import HttpResponse
import xlwt
=======
from .forms import DateForm
>>>>>>> 4de1b879939bf1b159ad2351e0972c0e6babc0f9


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


<<<<<<< HEAD
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


=======
>>>>>>> 4de1b879939bf1b159ad2351e0972c0e6babc0f9
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
<<<<<<< HEAD

=======
    print('rows', rows)
>>>>>>> 4de1b879939bf1b159ad2351e0972c0e6babc0f9
    for row in rows:
        row_num += 1

        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)
    wb.save(response)

    return response
<<<<<<< HEAD


=======
>>>>>>> 4de1b879939bf1b159ad2351e0972c0e6babc0f9
