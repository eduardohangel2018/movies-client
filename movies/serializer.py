from rest_framework import serializers
from movies.models import User, Movie


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'data_nasc']


class MovieSerializer(serializers.ModelSerializer):
    title = serializers.CharField()
    director = serializers.CharField()
    description = serializers.CharField()
    release_date = serializers.IntegerField()
    rt_score = serializers.IntegerField()