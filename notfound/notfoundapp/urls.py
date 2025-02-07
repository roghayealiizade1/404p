from django.urls import path
from . import views

urlpatterns = [
    path('courses_list',views.courses_list)
]
