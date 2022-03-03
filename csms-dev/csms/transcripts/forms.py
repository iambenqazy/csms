from django.forms import ModelForm
from django import forms
from .models import StudentDetail


class StudentDetailForm(ModelForm):
    class Meta:
        model = StudentDetail
        fields = "__all__"
        widgets = {
            'student_subjects': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super(StudentDetailForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
