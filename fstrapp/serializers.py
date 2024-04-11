from rest_framework import serializers

from .models import *
from rest_framework.serializers import ModelSerializer


class UsersSerializer(ModelSerializer):
    class Meta:
        model = Users
        fields = "__all__"


class CoordsSerializer(ModelSerializer):
    class Meta:
        model = Coords
        fields = "__all__"


class LevelSerializer(ModelSerializer):
    class Meta:
        model = Level
        fields = "__all__"


class ImagesSerializer(ModelSerializer):
    class Meta:
        model = Images
        fields = ['data', 'title']


class PerevalSerializer(ModelSerializer):
    user = UsersSerializer()
    coord_id = CoordsSerializer()
    level = LevelSerializer()
    images = ImagesSerializer(many=True)

    class Meta:
        model = Pereval
        fields = ['beauty_title', 'title', 'other_titles', 'connect', 'user', 'coord_id', 'level', 'images']

    def create(self, validated_data):
        user = validated_data.pop('user')
        coord_id = validated_data.pop('coord_id')
        level = validated_data.pop('level')
        images = validated_data.pop('images')

        current_user = Users.objects.filter(email=user['email'])
        if current_user.exists():
            user_serializer = UsersSerializer(data=user)
            user_serializer.is_valid(raise_exception=True)
            user = user_serializer.save()
        else:
            user = Users.objects.create(**user)

        coord_id = Coords.objects.create(**coord_id)
        level = Level.objects.create(**level)
        new_pereval = Pereval.objects.create(**validated_data, user=user, level=level, coord_id=coord_id)

        for img in images:
            data = img.pop('data')
            title = img.pop('title')
            Images.objects.create(pereval=new_pereval, data=data, title=title)

        return new_pereval
