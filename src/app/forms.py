from django import forms

from .models import Student, Course


class FormAddStudent(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('name',)

    courses = forms.ModelMultipleChoiceField(queryset=Course.objects.all(), initial=Course.objects.order_by('id').first())

    def save(self, *args, **kwargs):
        obj = super().save(*args, **kwargs)
        obj.course_set.set(self.cleaned_data['courses'])
        return obj


