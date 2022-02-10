from django.db import models
from django.urls import reverse


class Employee(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=500)
    slug = models.SlugField(unique=True)

    def get_absolute_url(self):
        return reverse('visit', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'employee'


class Visits(models.Model):
    date = models.DateField(auto_now_add=False)
    user = models.ForeignKey(Employee, on_delete=models.CASCADE)
    visited = models.BooleanField(default=False)
    time_start = models.TimeField(auto_now_add=False, blank=True, null=True)
    time_end = models.TimeField(auto_now_add=False, blank=True, null=True)
    reason = models.CharField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return f'Сотрудник {self.user.name} {self.date}'

    class Meta:
        ordering = ['-date']
        db_table = 'visit'
