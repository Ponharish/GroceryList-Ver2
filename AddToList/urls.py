from django.urls import path
from . import views


urlpatterns = [
    path('', views.addToListMenu, name = 'addToListMenu'),
    path('addToListConfirm', views.addToListConfirm, name = 'addToListConfirm'),
    path('ACKaddToList', views.ACKaddToList, name = 'ACKaddToList'),
]