from django.contrib import admin

from .models import Show

from django import forms
from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class ShowAdminForm(forms.ModelForm):
    banner = forms.CharField(label='Баннер', widget=CKEditorUploadingWidget())
    logo = forms.CharField(label='Логотип партнеров', widget=CKEditorUploadingWidget())
    last_images = forms.CharField(label='Фотография животных с прошлой выставки', widget=CKEditorUploadingWidget())
    result_images = forms.CharField(label='Фотография животных по завершению выставки', widget=CKEditorUploadingWidget())
    animals = forms.CharField(label='Фотография животных', widget=CKEditorUploadingWidget())
    class Meta:
        model = Show
        fields = '__all__'


class ShowAdmin(admin.ModelAdmin):
    form = ShowAdminForm


admin.site.register(Show, ShowAdmin)



