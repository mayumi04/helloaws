from django.urls import path
from .views import helloworldfunction, get_list

urlpatterns = [
    path('today/', helloworldfunction),
    path('list/', get_list),
]