from django.urls import path
from . import views


urlpatterns = [
    path('', views.createlistmenu, name = 'createlistmenu'),
    path('redirectintermediatecreatelist', views.redirectintermediatecreatelist, name = 'redirectintermediatecreatelist'),
    path('createlistformlist1', views.createlistformlist1, name = 'createlistformlist1'),
    path('createlistformlist2', views.createlistformlist2, name = 'createlistformlist2'),
    path('acknowledgeceeation', views.acknowledgeceeation, name = 'acknowledgeceeation'),

]