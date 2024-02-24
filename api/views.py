from django.shortcuts import render
from .serializers import StudentSerializer
from .models import Student
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

@api_view(['GET','POST','PUT','PATCH','DELETE'])
def student_api(request,id=None):

    if request.method == 'GET':
        if id is not None :
            stu = Student.objects.get(pk=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)

        stu = Student.objects.all()
        serializer = StudentSerializer(stu,many=True)
        return Response(serializer.data)


    if request.method == 'POST':

        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'})
            return Response(serializer.data,status=status.HTTP_201_CREATED)

        return Response(serializer.errors)

    if request.method == 'PUT':
        
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Update Complete'})
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_RQUEST)

    if request.method == 'PATCH':
        stu = Student.objects.get(pk=id)
        serializer=StudentSerializer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data update partial'})
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_RQUEST)


    if request.method == 'DELETE':
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'Data Deleted'})
        return Response(status=status.HTTP_204_NO_CONTENT)
        

        
        



        

        




