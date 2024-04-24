from django.urls import path,include
from django.http import HttpResponse
from . import views

def test_view(request):
    return HttpResponse("Testing URL configuration")

urlpatterns = [
    path('test/', test_view, name='test'),
    path('urban_home/', views.urbanpass, name = 'urban_home'),
    path('customer_list/', views.customer_list, name='customer_list'),
    path('collaborator_list/', views.collaborator_list, name='collaborator_list'),
    path('sold_event_list/', views.sold_event_list, name='sold_event_list'),
    path('info_event_list/', views.info_event_list, name='info_event_list'),
    path('specific_event_list/', views.specific_event_list, name='specific_event_list'),
    path('booking_event_list/', views.booking_event_list, name='booking_event_list'),
    path('promoter_event_list/', views.promoter_event_list, name='promoter_event_list'),
    path('rate_event_list/', views.rate_event_list, name='rate_event_list'),
    path('collaborator_event_list/', views.collaborator_event_list, name='collaborator_event_list'),
]