from django.urls import path
from .views import ShowDetail, EndedShowList

urlpatterns = [
    path('show/<slug:slug>/', ShowDetail.as_view(), name='show'),
    path('ended_show/', EndedShowList.as_view(), name='ended_show'),
]