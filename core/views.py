from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

from django.shortcuts import render
from .models import Project

def home(request):
    projects = Project.objects.all()
    return render(request, 'home.html', {'projects': projects})


def project_detail(request, id):
    project = Project.objects.get(id=id)
    return render(request, 'detail.html', {'project': project})

class Helloview(APIView):
    def get(self, request):
        return Response({"text":"Hello"})