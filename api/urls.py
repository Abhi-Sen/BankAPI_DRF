from django.urls import include, path
from banks_api import urls as banks_api_app_url

app_name = "api"

urlpatterns = [
    path("banks_api/", include(banks_api_app_url))
]
