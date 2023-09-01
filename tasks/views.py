from .serializers import CreateTaskSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated






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

