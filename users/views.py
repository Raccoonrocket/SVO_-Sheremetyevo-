from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.views import View
from django.shortcuts import render, redirect

from users.forms import UserCreationForm, DataForm


class Register(View):
    template_name = 'registration/register.html'

    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)


def index(request):
    if request.method == 'POST':
        threshold_value = request.POST.get('threshold_value')
        crusher_slot_size = request.POST.get('crusher_slot_size')
        # ore_data =
        return HttpResponse(f'<h2>Threshold_value= {threshold_value} ,  Crusher_slot_size= {crusher_slot_size}</h2>')
    else:
        data_form = DataForm()
        return render(request, 'index.html', {'form': data_form})