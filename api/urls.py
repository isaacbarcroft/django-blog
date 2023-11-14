from django.urls import path, include

app_name = "api_v1"

urlpatterns = [
    path('blogs/', include('blogs.urls',  namespace='blogs')),
    path('accounts/', include('accounts.urls',  namespace='accounts')),
]
