from django.shortcuts import render, redirect
from django.db.models import Count, Avg
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import login, logout
from .models import Usuario, Evento, EntradaXClientes, Valoracion, LugarEvento, Promotor
from django.http import HttpResponse
from .forms import UserRegisterForm
from .models import Evento
from .forms import UserRegisterForm, LoginForm
import re
# Create your views here.

def urbanpass(request):
    return render (request, "urbanpassApp/index.html")

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('contrasena')
            if not re.match(r'^(?=.*[A-Z])(?=.*\d)(?=.*[~!@#$%^&*()_+{}|:"<>?,./]).{8,}$', password):
                error_message = 'La contraseña debe contener al menos una letra mayúscula, un número y un carácter especial, y tener al menos 8 caracteres.'
            elif Usuario.objects.filter(nombre=username).exists() or Usuario.objects.filter(email=email).exists():
                error_message = 'El usuario ya está registrado.'
            else:
                # Guardar la contraseña encriptada en el modelo Usuario
                user = form.save(commit=False)
                user.contrasena = make_password(form.cleaned_data.get('contrasena'))
                last_id = Usuario.objects.latest('id_usuario').id_usuario
                new_id = last_id + 1
                user.id_usuario = new_id
                user.save()
                login(request, user)
                return redirect('../urban_home/')
    else:
        form = UserRegisterForm()
    return render(request, 'urbanpassApp/signup.html', {'form': form, 'error_message': error_message})

def customer_list(request):
    context = {'customer_list': Usuario.objects.filter(id_rol=1).all}
    return render (request, "urbanpassApp/customer_list.html", context)

def collaborator_list(request):
    context = {'collaborator_list': Usuario.objects.filter(id_rol=3).all}
    return render (request, "urbanpassApp/collaborator_list.html", context)

def sold_event_list(request):
    context = {'sold_event_list': EntradaXClientes.objects.filter(id_entrada__estado='Vendida').select_related('id_cliente', 'id_entrada')}
    return render (request, "urbanpassApp/sold_event_list.html", context)

def info_event_list(request):
    context = {'info_event_list': Evento.objects.select_related('id_lugar_evento')}
    return render (request, "urbanpassApp/info_event_list.html", context)

def specific_event_list(request):
    context = {'specific_event_list': Valoracion.objects.filter(id_evento__id_evento=1).select_related('id_cliente')}
    return render (request, "urbanpassApp/specific_event_list.html", context)

def booking_event_list(request):
    context = {'booking_event_list': EntradaXClientes.objects.filter(id_entrada__estado='Reservada').select_related('id_cliente', 'id_entrada')}
    return render (request, "urbanpassApp/booking_event_list.html", context)

def promoter_event_list(request):
    context = {'promoter_event_list': Evento.objects.select_related('id_promotor', 'id_lugar_evento')}
    return render (request, "urbanpassApp/promoter_event_list.html", context)

def rate_event_list(request):
    context = {'rate_event_list': Valoracion.objects.select_related('id_cliente', 'id_evento')}
    return render (request, "urbanpassApp/rate_event_list.html", context)

def collaborator_event_list(request):
    context = {'collaborator_event_list': Evento.objects.select_related('id_colaborador')}
    return render (request, "urbanpassApp/collaborator_event_list.html", context)

def signout(request):
    logout(request)
    return redirect('../urban_home/')

def signin(request):
    error_message = ''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            contrasena = form.cleaned_data['contrasena']
            try:
                usuario = Usuario.objects.get(email=email)
                if check_password(contrasena, usuario.contrasena):
                    login(request, usuario) 
                    return redirect('/urban_home/', {'usuario': usuario})  
                else:
                    error_message = 'La contraseña es incorrecta.'
            except Usuario.DoesNotExist:
                error_message = 'El usuario no existe.'
    else:
        form = LoginForm()
    return render(request, 'urbanpassApp/login.html', {'form': form, 'error_message': error_message })
def event_list(request):
    context = {'event_list': Evento.objects.all()}
    return render(request, 'urbanpassApp/event_list.html', context)

def client_ticket(request):
    context = {'client_ticket': EntradaXClientes.objects.filter(id_cliente='4').select_related('id_cliente', 'id_entrada')}
    return render(request, 'urbanpassApp/client_ticket.html', context)

