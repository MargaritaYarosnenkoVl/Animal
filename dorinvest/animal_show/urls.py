from django.urls import path, include
from .views import ShowList, ShowAdd, ShowDetail

urlpatterns = [
    path('', ShowList.as_view(), name='show'),
    path('add/', ShowAdd.as_view(), name='add'),
    path('<int:pk>', ShowDetail.as_view(), name='detail'),
    #path('add/', post, name='post'),
]