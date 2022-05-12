
# Create your views here.
from crypt import methods
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from .Serializer import BodypartSerializer , SymsSerializer
from rest_framework.response import Response
from .models import Bodypart , Symptom
from rest_framework.parsers import JSONParser

from user_from import Serializer




@csrf_exempt
@api_view(['POST', 'GET','DELETE'])
def bodypart(request):
    if request.method == 'GET':
        bodypart = Bodypart.objects.all()
        serializer = BodypartSerializer(bodypart, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request) 
        serializer =BodypartSerializer(data=data) 
        if serializer .is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        bodypart = Bodypart.objects.all()
        bodypart.delete()
        return Response(status=204)


@csrf_exempt
@api_view(['POST', 'GET','DELETE'])
def symptom(request):
    if request.method == 'GET':
        symptomname = Symptom.objects.all()
        Serializer = SymsSerializer(symptomname, many=True)
        return Response(Serializer.data)
    if request.method == 'POST':
        data = JSONParser().parse(request)
        Serializer = SymsSerializer(data=data)
        if Serializer.is_valid():
            Serializer.save()
            return Response(Serializer.data, status=201)
        return Response(Serializer.errors, status=400)
    elif request.method == 'DELETE':
        s = Symptom.objects.all()
        s.delete()
        return Response(status=204)

