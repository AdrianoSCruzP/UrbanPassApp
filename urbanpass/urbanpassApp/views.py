from django.shortcuts import render, redirect
from django.db.models import Count, Avg
from django.contrib.auth.hashers import make_password
from .models import Usuario, Evento, EntradaXClientes, Valoracion, LugarEvento, Promotor
from django.http import HttpResponse
from .forms import UserRegisterForm
from .models import Evento
# Create your views here.

def urbanpass(request):
    return render (request, "urbanpassApp/index.html")

def signup(request):
    error_message = None
    
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            if Usuario.objects.filter(nombre=username).exists() or Usuario.objects.filter(email=email).exists():
                error_message = 'El usuario ya está registrado.'
            else:
                # Guardar la contraseña encriptada en el modelo Usuario
                user = form.save(commit=False)
                user.contrasena = make_password(form.cleaned_data.get('contrasena'))
                last_id = Usuario.objects.latest('id_usuario').id_usuario
                new_id = last_id + 1
                user.id_usuario = new_id
                print(user)
                user.save()
                return redirect('../login/')
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

def login_view(request):
    return render(request, 'urbanpassApp/login.html')

def event_list(request):
    context = {'event_list': Evento.objects.all()}
    return render(request, 'urbanpassApp/event_list.html', context)

def client_ticket(request):
    context = {'client_ticket': EntradaXClientes.objects.filter(id_cliente='4').select_related('id_cliente', 'id_entrada')}
    return render(request, 'urbanpassApp/client_ticket.html', context)