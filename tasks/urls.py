from . import views
from django.urls import path

urlpatterns = [
    path("create",views.create_task,name="create-task"),
]