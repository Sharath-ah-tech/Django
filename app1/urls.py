from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
urlpatterns = [
    path('register/', UserCreateView.as_view(), name='register'),
   
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
   
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

    path('', user_create, name='index'),
    path('models/', models_page, name='models'),
    path('employee/', employee_page, name='employee'),
    path('tasks/', task_page, name='tasks'),
    path('projects/', project_page, name='projects'),
    path('orders/', order_page, name='orders'),
    path('certificates/', certificate_page, name='certificates'),
]