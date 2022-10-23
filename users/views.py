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
        date_time = request.POST.get('date_time')
        arrival_departure = request.POST.get('arrival_departure')
        number_of_pass = request.POST.get('number_of_pass')
        parking_place = request.POST.get('parking_place')
        gate_number = request.POST.get('gate_number')
        return HttpResponse(f'<h2>{date_time}, {arrival_departure}, {number_of_pass}, '
                            f'{parking_place}, {gate_number}</h2>') # plug
    else:
        data_form = DataForm()
        return render(request, 'index.html', {'form': data_form})