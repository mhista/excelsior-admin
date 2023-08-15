from django.shortcuts import render
from django.views import generic
# Create your views here.

class DepartmentView(generic.TemplateView):
    template_name = 'index-2.html'
    
class StudentView(generic.TemplateView):
    template_name = 'students.html'
class AboutView(generic.TemplateView):
    template_name = 'about.html'
    