from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from imageprocessingrequests.models import ImageProcessingRequest
from imageprocessingrequests.serializers import ImageProcessingRequestSerializer

@csrf_exempt
def imageprocessingrequest_list(request):
    """
    List all imageprocessingrequests, or create a new imageprocessingrequest.
    """
    if request.method == 'GET':
        imageprocessingrequest = ImageProcessingRequest.objects.all()
        serializer = ImageProcessingRequestSerializer(imageprocessingrequest, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ImageProcessingRequestSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def imageprocessingrequest_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        imageprocessingrequest = ImageProcessingRequest.objects.get(pk=pk)
    except ImageProcessingRequest.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ImageProcessingRequestSerializer(snippet)
        return JsonResponse(serializer.data)