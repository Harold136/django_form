from django import forms
from .models import languages, Post


class CreateForm(forms.ModelForm):
    student_name = forms.CharField(
        label="Student Name",
        required=True,
        error_messages={"required": "Student Name is required."},
    )
    student_id = forms.CharField(
        label="Student ID",
        required=True,
        error_messages={"required": "Student ID is required."},
    )
    languages = forms.MultipleChoiceField(
        choices=languages,
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Post
        fields = "__all__"
        widgets = {
            "class_standing": forms.RadioSelect,
        }

    def clean_languages(self):
        return ",".join(self.cleaned_data["languages"])