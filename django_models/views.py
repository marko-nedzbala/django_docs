from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from .forms import UploadFileForm, ContactForm
from .models import Contact, Publisher
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth import views as auth_views

# Create your views here.

def handle_uploaded_file():
    pass

def thanks(request):
    return render(request, 'django_models/thanks.html')

# def upload_file(request):
#     if request.method == 'POST':
#         form = UploadFileForm(request.POST, request.FILES)
#         if form.is_valid():
#             # handle_uploaded_file(request.FILES['file'])
#             print(request.FILES['file'])
#             # return redirect('django_models/upload.htm')
#             form.save()
#             return HttpResponseRedirect('thanks/')
#     else:
#         form = UploadFileForm()
#     return render(request, 'django_models/upload.html', {'form': form})

def save_example(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']

            contact = Contact(subject=subject, message=message, sender=sender, cc_myself=cc_myself)
            contact.save()

            # form.save()
            print('Saved')
            return HttpResponseRedirect('/thanks/')
            # return HttpResponseRedirect('http://localhost:8000/polls/')
            # return HttpResponseRedirect(reverse('polls:pandas'))
    else:
        form = ContactForm()

    return render(request, 'django_models/upload.html', {'form': form})



from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import NameForm


def example(request):
    context = {}
    context['form'] = NameForm()
    return render(request, 'django_models/upload.html', context)

class PublisherListView(ListView):
    model = Publisher
    context_object_name = 'publishers'

class PublisherCreateView(CreateView):
    model = Publisher
    fields = ['name']

class PublisherUpdateView(UpdateView):
    model = Publisher
    fields = ['name']

class PublisherDeleteView(DeleteView):
    model = Publisher
    success_url = reverse_lazy('pub-list')


class MyLogin(auth_views.LoginView):
    template_name = 'django_models:thanks.html'

class MyProfile(auth_views.LoginView):
    template_name = 'django_models/index.html'

