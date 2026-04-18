from django.db import models

class Employee(models.Model):   
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    position = models.CharField(max_length=200, default=" ")
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='tasks')

    def __str__(self):
        return self.title
    

class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    number_of_projects = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    

class Order(models.Model):
    order_number = models.CharField(max_length=100)
    order_date = models.DateField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.order_number


class Certificate(models.Model):
    certificate_name = models.CharField(max_length=200)
    issued_date = models.DateField()
    expiry_date = models.DateField()

    def __str__(self):
        return self.certificate_name