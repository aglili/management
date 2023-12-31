from . import views
from django.urls import path

urlpatterns = [
    path("create",views.create_task,name="create-task"),
    path("delete/<str:task_id>",views.delete_task,name="delete-task"),
    path("assign/<str:task_id>",views.assign_task,name="assign-task"),
    path("",views.get_tasks,name="get-tasks"),
    path("assigned",views.get_assigned_tasks,name="get-assigned-tasks")

]