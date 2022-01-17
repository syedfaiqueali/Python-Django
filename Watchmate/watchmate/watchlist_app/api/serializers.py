from rest_framework import serializers
from watchlist_app.models import Movie


### Helper Validation Functions
def name_length(value):
    if len(value) < 2:
        raise serializers.ValidationError("Name is too short")


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True) #read_only=true; Non-editable
    name = serializers.CharField(validators=[name_length])
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

    '''def validate(self, data):
        """Object level validation"""
        if data['name'] == data['description']:
            raise serializers.ValidationError("Name and Description should be different!")
        return value'''

    def validate_name(self, value):
        """Field level validation: To validate name"""
        if len(value) < 2:
            raise serializers.ValidationError("Name is too short")
        else:
            return value
