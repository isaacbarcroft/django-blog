from django.urls import path
from . import views

app_name = "blogs"


urlpatterns = [
    path('', views.BlogList.as_view(),  name='blog_list'),
]
