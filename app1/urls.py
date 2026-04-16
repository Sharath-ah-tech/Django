from django.urls import path
from .views import EmployeeListCreate, EmployeeRetrieveUpdateDestroy, TaskListCreate, TaskRetrieveUpdateDestroy, ProjectListCreate, ProjectRetrieveUpdateDestroy, OrderListCreate, OrderRetrieveUpdateDestroy, CertificateListCreate, CertificateRetrieveUpdateDestroy
urlpatterns = [
    path('Employee/', EmployeeListCreate.as_view(), name='employee-list'),
    path('Employee/<int:pk>/', EmployeeRetrieveUpdateDestroy.as_view(), name='employee-detail'),
    path('Task/', TaskListCreate.as_view(), name='task-list'),
    path('Task/<int:pk>/', TaskRetrieveUpdateDestroy.as_view(), name='task-detail'),
    path('Project/', ProjectListCreate.as_view(), name='project-list'),
    path('Project/<int:pk>/', ProjectRetrieveUpdateDestroy.as_view(), name='project-detail'),
    path('Order/', OrderListCreate.as_view(), name='order-list'),
    path('Order/<int:pk>/', OrderRetrieveUpdateDestroy.as_view(), name='order-detail'),
    path('Certificate/', CertificateListCreate.as_view(), name='certificate-list'),
    path('Certificate/<int:pk>/', CertificateRetrieveUpdateDestroy.as_view(), name='certificate-detail'),
]