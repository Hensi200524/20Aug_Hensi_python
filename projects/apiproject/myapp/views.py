from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# Create your views here.
@api_view(['GET'])
def getall(request):
    stdata = studinfo.objects.all()
    serial = studsearial(stdata,many=True)
    return Response(data=serial.data)

@api_view(['GET'])
def getsid(request,id):
    try:
        sid = studinfo.objects.get(id=id)
    except studinfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serial = studsearial(sid)
    return Response(data=serial.data)

@api_view(['GET','DELETE'])
def deletesid(request,id):
    try:
        sid = studinfo.objects.get(id=id)
    except studinfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serial = studsearial(sid)
        return Response(data=serial.data)
    
    if request.method == 'DELETE':
        studinfo.delete(sid)
        return Response(status=status.HTTP_202_ACCEPTED)
    
@api_view(['POST'])
def savedata(request):
    if request.method == 'POST':
        serial = studsearial(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['PUT','GET'])
def updatedata(request,id):
    try:
        sid = studinfo.objects.get(id=id)
    except studinfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serial = studsearial(sid)
        return Response(data=serial.data)
    
    if request.method == 'PUT':
        serial = studsearial(data=request.data,instance=sid)
        if serial.is_valid():
            serial.save()
            return Response(status=status.HTTP_202_ACCEPTED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    

    
