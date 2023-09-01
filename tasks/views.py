from .serializers import CreateTaskSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Task
from accounts.models import User






@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_task(request):
    try:
        serializer = CreateTaskSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(creator=request.user)
            return Response(
                {
                    "status":True,
                    "message":"Task Created"
                }
            ,status=201)
    except Exception as e:
        return Response(
            {
                "status":False,
                "error":str(e)
            }
        ,status=400)
    

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_task(request,task_id:str):
    try:
        task = Task.objects.get(pk=task_id)
        if task.creator == request.user:
            task.delete()
            return Response(
                {
                    "status":True,
                    "message":"Task Deleted"
                }
            ,status=200)
        else:
            return Response(
                {
                    "status":False,
                    "error":"Permission Denied"
                }
            ,status=403)
    except Task.DoesNotExist():
        return Response(
                {
                    "status":False,
                    "error":"Task Does Not Exists"
                }
            ,status=404)
    except Exception as e:
        return Response(
            {
                "status":False,
                "error":str(e)
            }
        ,status=400)
    

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def assign_task(request, task_id:str):
    try:
        task = Task.objects.get(pk=task_id)
        assignee_username = request.data.get("assignee_username")

        try:
            assignee = User.objects.get(username=assignee_username)
        except User.DoesNotExist:
            return Response(
                {
                    "status": False,
                    "error": "Assignee user does not exist."
                },
                status=404
            )

        if task.creator == request.user:
            task.creator = assignee
            task.save()

            return Response(
                {
                    "status": True,
                    "message": f"{request.user.username} assigned task '{task.title}' to '{assignee_username}'."
                },
                status=200
            )
        else:
            return Response(
                {
                    "status": False,
                    "error": "Permission denied. Only the task creator can assign the task."
                },
                status=403
            )

    except Task.DoesNotExist:
        return Response(
            {
                "status": False,
                "error": "Task not found."
            },
            status=404
        )

    except Exception as e:
        return Response(
            {
                "status": False,
                "error": str(e)
            },
            status=500
        )

        


    

        


