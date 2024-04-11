from django.contrib import admin

from .models import Show, Animals, Feedback, Banner, Story, Location, SociaLinks, Partners, EndedShow, Photoreport

from django import forms
from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class ShowAdmin(admin.ModelAdmin):
    """ Админ-панель модели выставки"""
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}


class AnimalsAdmin(admin.ModelAdmin):
    """ Админ-панель модели животных"""
    list_display = ('name', 'image_animals', 'description', 'category')
    list_display_links = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}



# class FeedbackAdmin(admin.ModelAdmin):
#     """ Админ-панель модели профиля"""
#     list_display = ('email', 'ip_address', 'user')
#     list_display_links = ('email', 'ip_address')


class FeedbackAdmin(admin.ModelAdmin):
    """ Админ-панель модели профиля"""
    list_display = ('name', 'user_phone')
    list_display_links = ('name',)


class BannerAdmin(admin.ModelAdmin):
    """ Админ-панель модели баннера"""
    list_display = ('name', 'banner')
    list_display_links = ('name',)


class StoryAdmin(admin.ModelAdmin):
    """ Админ-панель модели Счатливые истории"""
    list_display = ('name', 'story', 'photo')
    list_display_links = ('name',)


class LocationAdmin(admin.ModelAdmin):
    """ Админ-панель модели места проведения выставки"""
    list_display = ('place', 'phone', 'duration')
    list_display_links = ('place',)


class SociaLinksAdmin(admin.ModelAdmin):
    """ Админ-панель модели социальных ссылок"""
    list_display = ('name', 'social_link', 'social_logo')
    list_display_links = ('name',)


class PartnersAdmin(admin.ModelAdmin):
    """ Админ-панель модели партнеров"""
    list_display = ('name', 'logo', 'partners_link')
    list_display_links = ('name',)


# class EndedShowAdmin(admin.ModelAdmin):
#     """ Админ-панель модели прошедших выставок"""
#     prepopulated_fields = {'slug': ('title',)}
#
#     def save_related(self, request, form, formsets, change):
#         super().save_related(request, form, formsets, change)
#         if not change:
#             form.instance.photoreport.clear()
class EndedShowAdminForm(forms.ModelForm):
    class Meta:
        model = EndedShow
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        if not self.instance.pk:
            self.instance.photoreport.clear()
        return cleaned_data

class EndedShowAdmin(admin.ModelAdmin):
    form = EndedShowAdminForm
    prepopulated_fields = {'slug': ('title',)}

    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)
        if not change:
            form.instance.photoreport.clear()



admin.site.register(Show, ShowAdmin)
admin.site.register(Animals, AnimalsAdmin)
admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(Banner, BannerAdmin)
admin.site.register(Story, StoryAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(SociaLinks, SociaLinksAdmin)
admin.site.register(Partners, PartnersAdmin)
admin.site.register(EndedShow, EndedShowAdmin)
admin.site.register(Photoreport)



