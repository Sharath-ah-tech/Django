from rest_framework import generics
from .models import Employee, Task, Project, Order, Certificate
from .serializers import (
    EmployeeSerializer, TaskSerializer, ProjectSerializer,
    OrderSerializer, CertificateSerializer, UserSerializer
)
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def index(request):
    return render(request, 'index.html')

def models_page(request):
    return render(request, 'models.html')

def employee_page(request):
    return render(request, 'employee.html')

def task_page(request):
    return render(request, 'tasks.html')

def project_page(request):
    return render(request, 'projects.html')

def order_page(request):
    return render(request, 'orders.html')

def certificate_page(request):
    return render(request, 'certificates.html')

class UserCreateView(generics.CreateAPIView):
    serializer_class = UserSerializer 

def user_create(request):
    if request.method == "POST":
        username = request.POST.get("f")
        email = request.POST.get("e")
        password = request.POST.get("p")

        if username and email and password:

            # Create user (if not exists)
            user, created = User.objects.get_or_create(
                username=username,
                defaults={"email": email}
            )

            # Always set/update password
            user.set_password(password)
            user.save()

            # Authenticate + login
            user = authenticate(request, username=username, password=password)

            if user:
                login(request, user)
                return redirect('models')

    return render(request, 'index.html')

class EmployeeListCreate(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]

class EmployeeRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]

class TaskListCreate(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]


class TaskRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

class ProjectListCreate(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]


class ProjectRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]


class OrderListCreate(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]


class OrderRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]


class CertificateListCreate(generics.ListCreateAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer
    permission_classes = [IsAuthenticated]


class CertificateRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer
    permission_classes = [IsAuthenticated]
