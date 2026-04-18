from django.urls import path
from .views import *

urlpatterns = [
    path('Employee/', EmployeeListCreate.as_view()),
    path('Employee/<int:pk>/', EmployeeRetrieveUpdateDestroy.as_view()),

    path('Task/', TaskListCreate.as_view()),
    path('Task/<int:pk>/', TaskRetrieveUpdateDestroy.as_view()),

    path('Project/', ProjectListCreate.as_view()),
    path('Project/<int:pk>/', ProjectRetrieveUpdateDestroy.as_view()),

    path('Order/', OrderListCreate.as_view()),
    path('Order/<int:pk>/', OrderRetrieveUpdateDestroy.as_view()),

    path('Certificate/', CertificateListCreate.as_view()),
    path('Certificate/<int:pk>/', CertificateRetrieveUpdateDestroy.as_view()),
]