from django.urls import path, include
from .views import ShowList, ShowAdd, ShowDetail, AnimalsAdd, FeedbackCreateView

urlpatterns = [
    path('', ShowList.as_view(), name='show'),
    path('add/', ShowAdd.as_view(), name='add'),
    path('animals/', AnimalsAdd.as_view(), name='animals'),
    path('<int:pk>', ShowDetail.as_view(), name='detail'),
    path('feedback/', FeedbackCreateView.as_view(), name='feedback'),
#     path('add/', post, name='post'),
]