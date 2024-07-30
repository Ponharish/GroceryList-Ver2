from django.urls import path
from . import views


urlpatterns = [
    path('', views.mainpage, name = 'homePage'),
    # path('feedback', views.feedback, name = 'feedback'),
    path('download-db', views.download_db, name='download_db'),
]