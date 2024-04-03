from django.urls import path, include
from .views import ShowList, ShowAdd

urlpatterns = [
    path('', ShowList.as_view(), name='index'),
    path('add/', ShowAdd.as_view(), name='add'),
    #path('add/', post, name='post'),
]