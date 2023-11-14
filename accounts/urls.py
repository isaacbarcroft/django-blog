from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path('', views.ProfileList.as_view(),  name='user_list'),
]
