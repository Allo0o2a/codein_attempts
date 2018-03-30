from django.shortcuts import render
from .models import User, Project, Portfolio
from rest_framework import viewsets
from .serializers import UserSerializer, ProjectSerializer, PortfolioSerializer
from rest_framework.response import Response
from rest_framework.decorators import list_route

# Create your views here.

class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @list_route(methods=['get'])
    def get_search_user(self,request):
        queryset = User.objects.all()
        
        search_user_name = None
        search_email = None
        search_developer = None
        search_python = None
        search_java = None
        search_standard_c = None
        search_c_plus_plus = None
        search_other_language = None
        
        if 'search_user_name' in self.request.query_params:
            search_user_name = self.request.query_params['search_user_name']
        if search_user_name:
            queryset = queryset.filter(username=search_user_name)

        if 'search_email' in self.request.query_params:
            search_email = self.request.query_params['search_email']
        if search_email:
            queryset = queryset.filter(email=search_email)

##        if 'search_developer' in self.request.query_params:
##            search_developer = self.request.query_params['search_developer']
##        if search_developer:
##            queryset = queryset.filter(developer=search_developer)
           
        serializer = UserSerializer(queryset, many=True, context=self.get_serializer_context())
        return Response(serializer.data)

class PortfoliotView(viewsets.ModelViewSet):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer

class ProjectView(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    @list_route(methods=['get'])
    def get_search_proj(self,request):
        queryset = Project.objects.all()
        
        search_proj_name = None
        search_user_projs = None
        
        if 'search_proj_name' in self.request.query_params:
            search_proj_name = self.request.query_params['search_proj_name']
        if search_proj_name:
            queryset = queryset.filter(proj_name=search_proj_name)

        if 'search_user_projs' in self.request.query_params:
            search_user_projs = self.request.query_params['search_user_projs']
        if search_user_projs:
            queryset = queryset.filter(username=search_user_projs)
            
        serializer = ProjectSerializer(queryset, many=True, context=self.get_serializer_context())
        return Response(serializer.data)
