
from django.urls import path
from .views import DepartmentView,StudentView
app_name = 'department'

urlpatterns = [
    path('',DepartmentView.as_view(),name='department'),
    path('student/',StudentView.as_view(),name='department'),
    
]