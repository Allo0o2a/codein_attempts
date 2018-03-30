from rest_framework import serializers
from .models import User, Project, Portfolio
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        # you can either include all the fields from models, or excludes the ones you don't need.
        fields = ('username', 'email', 'developer')
##        fields = ('username', 'email', 'developer', 'python', 'java', 'standard_c', 'c_plus_plus', 'other_language')

class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        # you can either include all the fields from models, or excludes the ones you don't need.
        fields = ('user', 'port_image', 'created_at', 'updated_at')


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        # you can either include all the fields from models, or excludes the ones you don't need.
        fields = ('user', 'proj_name', 'proj_description','created_at', 'updated_at')

