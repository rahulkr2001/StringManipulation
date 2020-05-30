from django.urls import path
from . import views
urlpatterns = [
    path('',views.Home,name='home'),
    path('string',views.String,name='string'),
    path('remove',views.Remove,name='remove'),
]
