from django.urls import path
from . import views
urlpatterns = [
    path('auth/all', views.AuthList.as_view()),
    path('auth/<pk>', views.AuthDetail.as_view()),
]
