from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator

class UserSerialzer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','email','password')

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all())])
    class Meta:
        model = User
        fields = ('id','username','email','password')
        extra_kwargs = {'password':{'write_only':True}}

    def create(self,validate_data):
        user = User.objects.create_user(validate_data['username'],validate_data['email'],validate_data['password'])

        return user

class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    class Meta:
        model = User
        fields = ['email','password']

