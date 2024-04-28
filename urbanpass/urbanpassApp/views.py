from django.shortcuts import render, redirect,get_object_or_404
from django.db.models import Count, Avg
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import login, logout
from .models import Usuario, Evento, EntradaXClientes, Valoracion, LugarEvento, Promotor, TipoEntrada, Entrada,Cliente
from django.http import HttpResponse
from .forms import UserRegisterForm
from .models import Evento,EntradaXClientes,Entrada
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, LoginForm
from django.http import JsonResponse
import re
from django.contrib.sessions.models import Session
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
                user = Usuario.objects.get(email=email)
                if check_password(contrasena, user.contrasena):
                    login(request, user) 
                    return redirect('/urban_home/')  
                else:
                    error_message = 'La contraseña es incorrecta.'
            except Usuario.DoesNotExist:
                error_message = 'El correo no existe.'
    else:
        form = LoginForm()
    return render(request, 'urbanpassApp/login.html', {'form': form, 'error_message': error_message })

def event_list(request):
    context = {'event_list': Evento.objects.all()}
    return render(request, 'urbanpassApp/event_list.html', context)

def client_ticket(request):
    usuario = get_user_from_session_cookie(request)
    context = {'client_ticket': EntradaXClientes.objects.filter(id_cliente= usuario.id_usuario).select_related('id_cliente', 'id_entrada')}
    return render(request, 'urbanpassApp/client_ticket.html', context)

def get_user_from_session_cookie(request):
    session_key = request.COOKIES.get('sessionid')

    if session_key:
        try:
            session = Session.objects.get(session_key=session_key)
        except Session.DoesNotExist:
            return None

        session_data = session.get_decoded()

        user_id = session_data.get('_auth_user_id')

        if user_id:
            try:
                user = Usuario.objects.get(pk=user_id)
                return user
            except Usuario.DoesNotExist:
                return None
    return None

def reservar_entrada(request, id_evento):
    usuario = get_user_from_session_cookie(request)
    if usuario:
        cliente_id = usuario.id_usuario
        
        cliente = get_object_or_404(Cliente, id_cliente=cliente_id)

        ultima_entrada = Entrada.objects.latest('id_entrada')
        ultimo_id_entrada = ultima_entrada.id_entrada if ultima_entrada else 0
        
        nuevo_id_entrada = ultimo_id_entrada + 1
        tipo_entrada = TipoEntrada.objects.get(id_tipo_entrada=1)

        nueva_entrada = Entrada.objects.create(id_entrada=nuevo_id_entrada, estado='Reservada', id_evento_id=id_evento, id_tipo_entrada= tipo_entrada)
        nueva_entradaxcliente = EntradaXClientes.objects.create(id_entrada=nueva_entrada, id_cliente=cliente)

        entrada = get_object_or_404(Entrada, id_entrada=nuevo_id_entrada)
        entrada.estado = 'Reservada'
        entrada.save()

        return JsonResponse({'message': 'Entrada creada y estado actualizado a Reservada'})
    else:
        return JsonResponse({'error': 'No se ha iniciado sesión'})

def pay_ticket(request, id_entrada):
    user = get_user_from_session_cookie(request)
    if user:
        ticket = Entrada.objects.get(id_entrada = id_entrada)
        ticket.estado = 'Vendida'
        ticket.save()

        return JsonResponse({'message': 'Entrada Vendida'})
    else:
        return JsonResponse({'error': 'No se pudo vender no tiene plata'})

def delete_ticket(request, id_entrada):
    user = get_user_from_session_cookie(request)
    if user:
        ticket = EntradaXClientes.objects.get(id_entrada = id_entrada)
        ticket.delete()

        ticket = Entrada.objects.get(id_entrada = id_entrada)
        ticket.estado = 'Disponible'
        ticket.save()

        return JsonResponse({'message': 'Entrada Eliminada'})
    else:
        return JsonResponse({'error': 'No se pudo eliminar'})