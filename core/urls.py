from django.urls import path
from core import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_query/<selected_dork>', views.get_query, name='get_query'),
    path('search/<id>+<query>', views.search, name='search'),
]