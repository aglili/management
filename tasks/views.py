from .serializers import CreateTaskSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Task






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

    

        


