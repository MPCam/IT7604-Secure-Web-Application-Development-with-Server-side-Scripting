from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.
class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('sign_in')
    template_name = 'registration/register.html'

class SignInView(generic.FormView):
    form_class = AuthenticationForm
    success_url = reverse_lazy('book_list')
    template_name = 'registration/signin.html'

    