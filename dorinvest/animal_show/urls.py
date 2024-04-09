from django.urls import path, include
from .views import ShowDetail, EndedShowDetail, EndedShowList

urlpatterns = [
    path('show/<slug:slug>/', ShowDetail.as_view(), name='show'),
    path('ended_show', EndedShowList.as_view(), name='ended_show'),
    path('ended_show/<int:pk>', EndedShowDetail.as_view(), name='ended_show_detail'),
    # path('show/', FeedbackCreate.as_view(), name='feedback'),
]