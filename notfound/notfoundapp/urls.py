from django.urls import path
from . import views

urlpatterns = [
    path('courses_list',views.courses_list),
    path('courses2',views.courses2)
]
