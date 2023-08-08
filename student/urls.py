from django.urls import path
from .views import CreateStudent,CreateGuardian,StudentDetail, IndexView
app_name = 'student'

urlpatterns = [
    path('register-student/',CreateStudent.as_view(),name='create-student'),
    path('register-parent/',CreateGuardian.as_view(),name='create-parent'),
    path('',IndexView.as_view(),name='index'),
    path('student-detail/<int:pk>/',StudentDetail.as_view(),name='student-detail'),
    
    
   
    
]