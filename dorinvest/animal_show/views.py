from django.contrib.messages.views import SuccessMessageMixin
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DetailView
from django.shortcuts import render
from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect, request
from django.views.generic.edit import FormMixin

from .forms import ShowForm, AnimalsForm, FeedbackCreateForm
from .models import Show, Animals, Feedback
from .services.email import send_contact_email_message
from .services.utils import get_client_ip


class ShowList(ListView):
    model = Show
    ordering = 'id'
    template_name = 'show.html'
    context_object_name = 's'
    form_class = ShowForm


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ShowForm()
        return context

    def get_initial(self):
        initial = super().get_initial()
        initial['user'] = self.request.user
        return initial



class ShowAdd(CreateView):
    model = Show
    form_class = ShowForm
    template_name = 'add.html'

    def get_initial(self):
        initial = super().get_initial()
        initial['user'] = self.request.user
        return initial


class AnimalsAdd(CreateView):
    model = Animals
    form_class = AnimalsForm
    template_name = 'animals.html'

    def get_initial(self):
        initial = super().get_initial()
        initial['user'] = self.request.user
        return initial

    def form_valid(self, form):
        user = self.request.user
        self.object = form.save(commit=False)
        self.object.user = user
        self.object.save()
        return super().form_valid(form)




class ShowDetail(FormMixin, DetailView):
    model = Show
    template_name = 'show.html'
    context_object_name = 'show'
    form_class = ShowForm
    queryset = Show.objects.all()
    success_message = 'Ваше письмо успешно отправлено администрации сайта'
    success_url = reverse_lazy('show')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        show = self.get_object()
        animals = show.animals.all()
        context['animals'] = animals
        context['feedback_form'] = FeedbackCreateForm()
        return context



class FeedbackCreateView(SuccessMessageMixin, CreateView):
    model = Feedback
    form_class = FeedbackCreateForm
    success_message = 'Ваше письмо успешно отправлено администрации сайта'
    template_name = 'show.html'
    extra_context = {'title': 'Контактная форма'}
    # success_url = reverse_lazy('detail')


    def form_valid(self, form):
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.ip_address = get_client_ip(self.request)
            if self.request.user.is_authenticated:
                feedback.user = self.request.user
            send_contact_email_message(feedback.subject, feedback.email, feedback.content, feedback.ip_address, feedback.user_id)
        return super().form_valid(form)

    def get_success_url(self):
        # Возвращаем URL текущего объекта, если он доступен
        if hasattr(self, 'object') and self.object is not None:
            return reverse('detail', kwargs={'pk': self.object.pk})
        # Или возвращаем URL по умолчанию
        return reverse('default_url')