from django.forms import ModelForm
from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Show


class ShowForm(ModelForm):
    class Meta:
        model = Show
        fields = '__all__'

#
# class AnimalsForm(ModelForm):
#     class Meta:
#         model = Animals
#         fields = ['image', 'description', 'category']
#
#
# class ImageForm(forms.ModelForm):
#     images = forms.ImageField(label='фото')
#
#     class Meta:
#         model = Image
#         fields = ('images', )
#
# class MultipleFileInput(forms.ClearableFileInput):
#     allow_multiple_selected = True
#
# class MultipleFileField(forms.FileField):
#     def __init__(self, *args, **kwargs):
#         kwargs.setdefault("widget", MultipleFileInput())
#         super().__init__(*args, **kwargs)
#
#     def clean(self, data, initial=None):
#         single_file_clean = super().clean
#         if isinstance(data, (list, tuple)):
#             result = [single_file_clean(d, initial) for d in data]
#         else:
#             result = single_file_clean(data, initial)
#         return result
#
# class FullForm(forms.ModelForm):
#     images = MultipleFileField(label='Image', required=False)
#
#     class Meta(ShowForm.Meta):
#         fields = ShowForm.Meta.fields + ['images', ]