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

from .forms import ShowForm, AnimalsForm, FeedbackCreateForm, EndedShowForm
from .models import Show, Animals, Feedback, EndedShow


# from .services.email import send_contact_email_message
# from .services.utils import get_client_ip


class ShowDetail(FormMixin, DetailView):
    model = Show
    template_name = 'show.html'
    context_object_name = 'show'
    form_class = ShowForm
    queryset = Show.objects.all()


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        show = self.get_object()
        animals = show.animals.all()
        banners = show.banners.all()
        stores = show.stores.all()
        locations = show.locations.all()
        social_links = show.social_links.all()
        partners = show.partners.all()
        context['animals'] = animals
        context['banners'] = banners
        context['stores'] = stores
        context['locations'] = locations
        context['social_links'] = social_links
        context['partners'] = partners
        context['feedback_form'] = FeedbackCreateForm()
        return context


class FeedbackCreate(CreateView):
    model = Feedback
    form_class = FeedbackCreateForm
    template_name = 'show.html'
    success_url = reverse_lazy('/')


class EndedShowList(ListView):
    model = EndedShow
    ordering = '-id'
    template_name = 'ended_show_list.html'
    context_object_name = 'endedshow'
    paginate_by = 6
    form_class = EndedShowForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = EndedShowForm
        return context



class EndedShowDetail(FormMixin, DetailView):
    model = EndedShow
    template_name = 'EndedShow.html'
    context_object_name = 'ended_show'
    form_class = EndedShowForm
    queryset = EndedShow.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ended_show = self.get_object()
        photoreport = ended_show.photoreport.all()
        context['photoreport'] = photoreport
        return context
