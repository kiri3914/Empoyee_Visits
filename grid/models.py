from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=500)

    class Meta:
        db_table = 'employee'


class Visits(models.Model):
    data = models.DateField(auto_now_add=False)
    user = models.ForeignKey(Employee, on_delete=models.CASCADE)
    posetil = models.BooleanField(default=False)
    time_start = models.DateTimeField(auto_now_add=False, blank=True, null=True)
    time_end = models.DateTimeField(auto_now_add=False, blank=True, null=True)
    prichina = models.CharField(max_length=1000, blank=True, null=True)

