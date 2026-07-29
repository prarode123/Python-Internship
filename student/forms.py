from django import forms
from .models import Student


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ['name', 'course', 'email']

    def clean_name(self):
        name = self.cleaned_data['name']

        if any(char.isdigit() for char in name):
            raise forms.ValidationError(
                "Name should not contain numbers."
            )

        return name

    def clean_email(self):
        email = self.cleaned_data['email']

        if Student.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError(
                "Email already exists."
            )

        return email