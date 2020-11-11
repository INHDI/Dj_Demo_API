from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from home.models import Klee
from home.serializers import KleeSerializer
from django.contrib import messages
from django.contrib.auth import authenticate, login


# Create your views here.

def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('api_list')
        else:
            messages.info(request, 'Sai User hoặc Password')
    return render(request, 'home/login.html', )


@csrf_exempt
@login_required
def klee_list(request):
    if request.method == 'GET':
        klee = Klee.objects.all()
        serializers = KleeSerializer(klee, many=True)
        return JsonResponse(serializers.data, safe=False)
        # return HttpResponse(serializers.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializers = KleeSerializer(data=data)
        if serializers.is_valid():
            serializers.save
            return JsonResponse(serializers.data, status=201)
        return JsonResponse(serializers.errors, status=400)

@login_required
@csrf_exempt
def klee_details(request, pk):
    try:
        klee = Klee.objects.get(pk=pk)
    except Klee.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializers = KleeSerializer(klee)
        return JsonResponse(serializers.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializers = KleeSerializer(klee, data=data)
        if serializers.is_valid():
            serializers.save()
            return JsonResponse(serializers.data)
        return JsonResponse(serializers.errors, status=400)
    elif request.method == 'DELETE':
        klee.delete()
        return HttpResponse(status=204)


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)


class KleeView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        if request.method == 'GET':
            klee = Klee.objects.all()
            serializers = KleeSerializer(klee, many=True)
            return JsonResponse(serializers.data, safe=False)
            # return HttpResponse(serializers.data)
        elif request.method == 'POST':
            data = JSONParser().parse(request)
            serializers = KleeSerializer(data=data)
            if serializers.is_valid():
                serializers.save
                return JsonResponse(serializers.data, status=201)
            return JsonResponse(serializers.errors, status=400)

class KleeViewID(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request,pk):
        try:
            klee = Klee.objects.get(pk=pk)
        except Klee.DoesNotExist:
            return HttpResponse(status=404)
        if request.method == 'GET':
            serializers = KleeSerializer(klee)
            return JsonResponse(serializers.data)
        elif request.method == 'PUT':
            data = JSONParser().parse(request)
            serializers = KleeSerializer(klee, data=data)
            if serializers.is_valid():
                serializers.save()
                return JsonResponse(serializers.data)
            return JsonResponse(serializers.errors, status=400)
        elif request.method == 'DELETE':
            klee.delete()
            return HttpResponse(status=204)


