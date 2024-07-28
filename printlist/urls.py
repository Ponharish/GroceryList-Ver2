from django.urls import path
from . import views


urlpatterns = [
    path('', views.printlistmenu, name = 'printlistmenu'),
    path('redirectintermediateprintlist', views.redirectintermediateprintlist, name = 'redirectintermediateprintlist'),
    path('printlistformlist1', views.printlistformlist1, name = 'printlistformlist1'),
    path('printlistformlist2', views.printlistformlist2, name = 'printlistformlist2'),
    
]