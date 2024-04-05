from django.contrib import admin

from .models import Show, Animals, Feedback

from django import forms
from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class ShowAdminForm(forms.ModelForm):
    # banner = forms.CharField(label='Баннер', widget=CKEditorUploadingWidget())
    # logo = forms.CharField(label='Логотип партнеров', widget=CKEditorUploadingWidget())
    # last_images = forms.CharField(label='Фотография животных с прошлой выставки', widget=CKEditorUploadingWidget())
    # result_images = forms.CharField(label='Фотография животных по завершению выставки', widget=CKEditorUploadingWidget())


    class Meta:
        model = Show
        fields = '__all__'

        widgets = {
            'user': forms.HiddenInput(),
        }




class ShowAdmin(admin.ModelAdmin):
    form = ShowAdminForm

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)



class FeedbackAdmin(admin.ModelAdmin):
    """
    Админ-панель модели профиля
    """
    list_display = ('email', 'ip_address', 'user')
    list_display_links = ('email', 'ip_address')


admin.site.register(Show, ShowAdmin)
admin.site.register(Animals)
admin.site.register(Feedback)



