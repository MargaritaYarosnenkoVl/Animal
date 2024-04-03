from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.shortcuts import render
from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect, request

from .forms import ShowForm, ImageForm, FullForm, AnimalsForm
from .models import Show, Image, Animals


class ShowList(ListView):
    model = Show
    ordering = 'id'
    template_name = 'show.html'
    context_object_name = 'show'



class ShowAdd(CreateView):
    model = Show
    form_class = FullForm
    template_name = 'add.html'

    def get_initial(self):
        initial = super().get_initial()
        initial['user'] = self.request.user
        return initial
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