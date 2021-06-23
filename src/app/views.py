from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic.edit import ModelFormMixin

from .models import Student, Connect, Course


def index(request):
    return render(request,'base.html')


class CreateStudent(LoginRequiredMixin, CreateView):
    login_url = '/admin/'
    redirect_field_name = 'index'
    template_name = 'app/create_student.html'
    model = Student
    fields = ('name',)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        for student in form.cleaned_data['name']:
            connect = Connect()
            connect.student = self.object
            connect.course = Course.objects.get(name='math') #default math
            connect.save()
        return super(ModelFormMixin, self).form_valid(form)

# def UpdateDefaultB









