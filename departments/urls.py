
from django.urls import path
from .views import DepartmentView,StudentView,AboutView
app_name = 'department'

urlpatterns = [
    path('',DepartmentView.as_view(),name='index'),
    path('about/',AboutView.as_view(),name='about'),
    path('student/',StudentView.as_view(),name='department'),
    
]