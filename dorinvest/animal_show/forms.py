from django.forms import ModelForm
from django import forms

from .models import Show, Animals, Feedback


class ShowForm(ModelForm):
    class Meta:
        model = Show
        fields = '__all__'
        widgets = {
            'user': forms.HiddenInput(),
        }



class AnimalsForm(ModelForm):
    class Meta:
        model = Animals
        fields = '__all__'


class FeedbackCreateForm(forms.ModelForm):
    """Форма отправки обратной связи"""
    class Meta:
        model = Feedback
        fields = ('subject', 'email', 'content')

    def __init__(self, *args, **kwargs):
        """  Обновление стилей формы"""
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control', 'autocomplete': 'off'})