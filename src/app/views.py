from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import CreateView

from .forms import FormAddStudent


def index(request):
    return render(request, 'base.html')


class CreateStudent(LoginRequiredMixin, CreateView):
    login_url = '/admin/'
    redirect_field_name = 'index'
    form_class = FormAddStudent
    template_name = 'app/create_student.html'
    success_url = '/'


