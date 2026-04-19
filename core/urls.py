from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.Helloview.as_view(), name="hello"),
    path('go/', views.home),
    path('project/<int:id>/', views.project_detail),
]
