from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    confirm = serializers.CharField(max_length=120, write_only=True)
    
    def validate(self, data):
        pswrd = data.get("password")
        cnfrm = data.get("confirm")
        if pswrd != None and cnfrm != None and pswrd != cnfrm:
            raise serializers.ValidationError("Iltimos parolni to'gri takrorlang!")
        del data['confirm']
        return data

    class Meta:
        model = User
        fields = ['username', 'confirm', 'password']
    
    def create(self, validated_data):
        user = User(
        username=validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class SignInOutSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }
