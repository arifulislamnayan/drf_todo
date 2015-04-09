from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from task.models import Task
from api.serializers import TaskSerializer


@api_view(['GET', 'POST'])
def task_list(request):
    
    if request.method == 'GET':
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)


    elif request.method=='POST':
    	serializer= TaskSerializer(data=request.DATA)
    	if serializer.is_valid():
    		serializer.save()
    		return Response(serializer.data, status=status.HTTP_201_CREATED)

    	else:
    		return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)



    		
