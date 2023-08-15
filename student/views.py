from typing import Any, Dict
from django.db import models
from django.shortcuts import render
from django.views import generic
from .mixins import CreateUpdateStudent
from school.file_upload import file_ext, profile_upload
from .models import Guardian,Student
from  django.http import JsonResponse
from school.models import Data

class IndexView(generic.TemplateView):
    template_name = "about.html"
    
class CreateStudent(CreateUpdateStudent,generic.View):
    def get(self,*args,**kwargs):
        from departments.models import Grade 
        std_class = Grade.objects.all()
        context = {'class':std_class}
        
        return render(self.request,'add_students.html',context)
    def post(self,request,*args,**kwargs,):
        from departments.models import Grade 
        self.unique_ref=request.POST.get('unique_ref')  
        get_data = Data.objects.filter(unique_ref=self.unique_ref)
        if get_data.exists():
            return JsonResponse({'data':f'already saved in the database','saved':False})
        else:
            data = Data.objects.create(
                gender=request.POST.get('gender'),
                photo=request.FILES.get('photo'),
                age=request.POST.get('age'),
                unique_ref=self.unique_ref
            )
            Student.objects.create(
                data=data,
                firstname=request.POST.get('firstname'),
                lastname=request.POST.get('lastname'),
                dob=request.POST.get('dob'),
                std_class=Grade.objects.get(id=request.POST.get('class')),
            )
            get_data = Data.objects.filter(unique_ref=self.unique_ref)
            if get_data.exists() and len(get_data) > 1:
                to_delete = get_data[1:]
                for x in to_delete:
                    print(x)
                    x.delete()
                student_id=Student.objects.get(data=get_data[0]).id
                return JsonResponse({'data':f'successfully registered student', 'std_id':student_id,'saved':True})
class CreateGuardian(CreateUpdateStudent,generic.View):
    def post(self,request,*args,**kwargs): 
        self.unique_ref=request.POST.get('unique_ref')  
        get_data = Data.objects.filter(unique_ref=self.unique_ref)
        guard = request.POST.get('guardian')
        if get_data.exists():
            return JsonResponse({'data':f'already saved in the database','saved':False})
        else:
            if Data.DoesNotExist:
                data = Data.objects.create(
                gender=request.POST.get('gender'),
                photo=request.FILES.get('p_photo'),
                age=request.POST.get('p_age'),
                email=request.POST.get('email'),
                address=request.POST.get('address'),
                unique_ref=self.unique_ref  
                )
                guardian = Guardian.objects.create(
                    data=data,
                    name=request.POST.get('name'),
                    phone=request.POST.get('phone'),
                    student = Student.objects.get(id=guard)
                    
                )
                get_data = Data.objects.filter(unique_ref=self.unique_ref)
                if get_data.exists() and len(get_data) > 1:
                    to_delete = get_data[1:]
                    for x in to_delete:
                        print(x)
                        x.delete()
                    std_data = Student.objects.get(id=guard)
                    return JsonResponse({'data':f'successfully registered guardian for {std_data.firstname}','saved':True,'std_id':std_data.id})
class StudentDetail(generic.DetailView):
    context_object_name='student'
    template_name = 'students-profile.html'
    def get_queryset(self):
        self.pk = self.kwargs.get('pk')
        self.queryset = Student.objects.filter(pk=self.pk)        
        return self.queryset
    def get_context_data(self, **kwargs):
        from departments.models import Grade 
        context = super().get_context_data(**kwargs)
        context['data'] = Data.objects.get(student__pk=self.pk)
        context['guardian'] = Guardian.objects.get(student__pk=self.pk)
        context['grade'] = Grade.objects.get(student__pk=self.pk)
        return context
# class UpdateStudent(CreateUpdateStudent,generic.View):
#     def get(self,*args,**kwargs):
#         from departments.models import Grade 
        
        
    
    
    