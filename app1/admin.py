from django.contrib import admin
from .models import Employee, Task, Project, Order, Certificate
# Register your models here.
admin.site.register(Employee)
admin.site.register(Task)
admin.site.register(Project)
admin.site.register(Order)
admin.site.register(Certificate)
