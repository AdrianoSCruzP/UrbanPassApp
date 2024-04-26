from django.shortcuts import render
from django.db.models import Count, Avg
from .models import Usuario, Evento, EntradaXClientes, Valoracion, LugarEvento, Promotor
from django.http import HttpResponse

# Create your views here.

def urbanpass(request):
    return HttpResponse("Welcome to UrbanPass")

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