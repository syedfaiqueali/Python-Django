from rest_framework import serializers
from watchlist_app.models import Movie

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True) #read_only=true; Non-editable
    name = serializers.CharField()
    description = serializers.CharField()
    active = serializers.BooleanField()

    def create(self, validated_data):
        # Used in POST req
        return Movie.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # 1- Find the data and update it
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.active = validated_data.get('active', instance.active)

        # 2- Save and return it
        instance.save()
        return instance
