from unittest.util import _MAX_LENGTH
from rest_framework import serializers
from users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    #Redefinido el metodo create del serializador user para guardar la contraseña encriptada
    def create(self,validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
    #redefinido el meotod uodated del serializardor para guardar la contraseña encriptada
    def update(self,instance,validated_data):
        updated_user = super().update(instance,validated_data)
        updated_user.set_password(validated_data['password'])
        updated_user.save()
        return updated_user

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

    def to_representation(self, instance):
        return {
            'id' : instance['id'],
            'username' : instance['username'],
            'password' : instance['password'],
            'email' : instance['email'],
        }