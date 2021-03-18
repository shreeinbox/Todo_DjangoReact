#from django.shortcuts import render
#from django.http import JsonResponse


#Getting response in JSON format
#def apiOverview(request):
#    return JsonResponse("API BASE POINT", safe=False)


# to use api view in Response
from rest_framework.decorators import api_view
from rest_framework.response import Response

# We use serialisers to see the model data as JSON objects
from .serializers import TaskSerializer
# import model
from .models import Task

data = [
    {"id":1, "title": "School admission", "completed":False},
    {"id":2, "title": "EB bill", "completed":True},
]

@api_view(['GET'])
def apiOverview(request):
    api_url = {
        'List':'/task-list/',
        'Detail View':'/task-detail/<str:pk>/',
        'Create':'/task-create/',
        'Update':'/task-update/<str:pk>/',
        'Delete':'/task-delete/<str:pk>/',
        }
    return Response(api_url)

@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all().order_by('-id')
    #tasks = data
    #serializer here JSONify model data
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def taskDetail(request, pk):
    tasks = Task.objects.get(id=pk)
    serializer = TaskSerializer(tasks, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def taskCreate(request):
    serializer = TaskSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def taskUpdate(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def taskDelete(request, pk):
    task = Task.objects.get(id=pk)
    taskname = task.title
    task.delete()

    return Response("Item Deleted: " + taskname)

