from django.urls import path
from .views import *

urlpatterns=[
  path('home/',home),
  path('create/',create_task),
  path('delete/<int:id>/',delete_task),
  path('edit/<int:id>/',edit_task),
]