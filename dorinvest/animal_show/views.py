from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from django.shortcuts import render
from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect, request
from django.views.generic.edit import FormMixin

from .forms import ShowForm
from .models import Show


class ShowList(ListView):
    model = Show
    ordering = 'id'
    template_name = 'show.html'
    context_object_name = 'show'
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


class ShowDetail(FormMixin, DetailView):
    model = Show
    template_name = 'show.html'
    context_object_name = 'show_d'
    form_class = ShowForm
    queryset = Show.objects.all()

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        pk = self.kwargs.get('pk')
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form, **kwargs):
        try:
            self.object = form.save(commit=False)
            self.object.user = self.request.user
            self.object.post = self.get_object()
            self.object.save()
            return super().form_valid(form)
        except IntegrityError:
            return redirect('/')

    def get_success_url(self, **kwargs):
        return reverse_lazy('', kwargs={'pk': self.get_object().id})



#
#     def post(self, request, *args, **kwargs):
#         ImageFormSet = modelformset_factory(Image, form=ImageForm, extra=3)
#         if request.method == 'POST':
#             form = self.form_class(request.POST)
#             formset = ImageFormSet(request.POST, request.FILES, queryset=Image.objects.none())
#
#             if form.is_valid() and formset.is_valid():
#                 show_form = form.save(commit=False)
#                 show_form.user = request.user
#                 show_form.save()
#
#                 for form in formset.cleaned_data:
#                     if form:
#                         images = form['images']
#                         photo = Image(show=show_form, images=images)
#                         photo.save()
#                 messages.success(request, "Картинки добавлены")
#                 return HttpResponseRedirect("/")
#             else:
#                 print(form.errors, formset.errors)
#         else:
#             form = self.form_class()
#             formset = ImageFormSet(queryset=Image.objects.none())
#         return render(request, self.template_name, {'form': form, 'formset': formset})
#
# def addShowView(request):
#     if request.method == "POST":
#         #images will be in request.FILES
#         form = FullForm(request.POST or None, request.FILES or None)
#         files = request.FILES.getlist('images')
#         if form.is_valid():
#             user = request.user
#             banner = form.cleaned_data['banner']
#             logo = form.cleaned_data['logo']
#             last_images = form.cleaned_data['last_images']
#             result_images = form.cleaned_data['result_images']
#             show_obj = Show.objects.create(user=user,banner=banner,logo=logo, last_images=last_images, result_images=result_images)
#             image = form.cleaned_data['image']
#             animals_obj = Animals.objects.create(image=image)
#
#             for f in files:
#                 Image.objects.create(show=show_obj, animals=animals_obj, image=f)
#
#
#     else:
#         print("Form invalid")


# def post(self, request, *args, **kwargs):
#         ImageFormSet = modelformset_factory(Image, form=ImageForm, extra=3)
#         if request.method == 'POST':
#             form = self.form_class(request.POST)
#             formset = ImageFormSet(request.POST, request.FILES, queryset=Image.objects.none())
#
#             if form.is_valid() and formset.is_valid():
#                 show_form = form.save(commit=False)
#                 show_form.user = request.user
#                 show_form.save()
#
#                 for form in formset.cleaned_data:
#                     if form:
#                         images = form['images']
#                         photo = Image(show=show_form, images=images)
#                         photo.save()
#                 messages.success(request, "Картинки добавлены")
#                 return HttpResponseRedirect("/")
#             else:
#                 print(form.errors, formset.errors)
#         else:
#             form = self.form_class()
#             formset = ImageFormSet(queryset=Image.objects.none())
#         return render(request, self.template_name, {'form': form, 'formset': formset})

# @login_required
# def post(request):
#     ImageFormSet = modelformset_factory(Image,
#                                         form=ImageForm, extra=3)
#     # 'extra' means the number of photos that you can upload   ^
#     if request.method == 'POST':
#
#         showForm = ShowForm(request.POST)
#         formset = ImageFormSet(request.POST, request.FILES,
#                                queryset=Image.objects.none())
#
#         if showForm.is_valid() and formset.is_valid():
#             show_form = showForm.save(commit=False)
#             show_form.user = request.user
#             show_form.save()
#
#             for form in formset.cleaned_data:
#                 # this helps to not crash if the user
#                 # do not upload all the photos
#                 if form:
#                     images = form['images']
#                     photo = Image(post=show_form, images=images)
#                     photo.save()
#             # use django messages framework
#             messages.success(request,
#                              "Yeeew, check it out on the home page!")
#             return HttpResponseRedirect("/")
#         else:
#             print(showForm.errors, formset.errors)
#     else:
#         showForm = ShowForm()
#         formset = ImageFormSet(queryset=Image.objects.none())
#     return render(request, 'add.html',
#                   {'postForm': showForm, 'formset': formset})