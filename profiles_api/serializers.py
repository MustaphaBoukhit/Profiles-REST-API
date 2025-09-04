from rest_framework import serializers
from profiles_api import models

class HelloSerializer(serializers.Serializer):
    """ Seruializes a name field for testing out APIView """
    name = serializers.CharField(max_length=10)

class UserProfileSerializer(serializers.ModelSerializer):
    """ Serializes a user profile object """

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }
        #fields = ('email', 'name')

    def create(self, validated_data):
        """ Create and return a new user """
        print(validated_data)
        user = models.UserProfile.objects.create_user(
            email = 'm.boukhi12t@gasds.fr', #validated_data['email'],
            name = 'mustapha', #validated_data['name'],
            password = 'hello123' #validated_data['password']
        )
        return user


""" class UserProfileSerializer(serializers.ModelSerializer):
    ""Serializes a user profile object""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        ""Create and return a new user""
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )

        return user """

 