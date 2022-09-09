from django.urls import path, include
from . import views

urlpatterns = [
    path('farthest_frontier', views.farthest_frontier, name='farthest_frontier'),
    path('snow_runner', views.snow_runner, name='snow_runner'),

]
