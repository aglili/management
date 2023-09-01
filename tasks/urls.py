from . import views
from django.urls import path

urlpatterns = [
    path("create",views.create_task,name="create-task"),
    path("delete/<str:task_id>",views.delete_task,name="delete_task")
]