from rest_framework import serializers
from django.core import exceptions
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.models import AnonymousUser
from .models import User


class RegisterUserSerializers(serializers.ModelSerializer):
    password2 = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'password2')
        extra_kwargs = {'password': {"write_only": True}}

    def validate(self, attrs):
        if attrs.get("password") != attrs.get("password2"):
            raise serializers.ValidationError(
                {"detail": "password dose not math try again!"})
        try:
            validate_password(attrs.get("password"))
        except exceptions.ValidationError as e:
            raise serializers.ValidationError({"password": list(e.messages)})

        return super().validate(attrs)

    def create(self, validated_data):
        validated_data.pop("password2", None)
        return User.objects.create_user(**validated_data)


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(write_only=True, required=True)
    password = serializers.CharField(write_only=True, required=True)
    password2 = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = User
        fields = ('old_password', 'password', 'password2')

    def validate(self, attrs):
        if attrs.get('password') != attrs.get('password2'):
            raise serializers.ValidationError(
                {'detail': 'Passwords Does Not match'})

        try:
            validate_password(attrs.get('password'))
        except exceptions.ValidationError as e:
            raise serializers.ValidationError({"password": list(e.messages)})

        return super().validate(attrs)

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError(
                {'detail': 'The provided old password is incorrect.'})


class ProfileUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def to_representation(self, instance):
        
        if isinstance(instance, AnonymousUser):
            return {'detail': 'User Not Authenticated'}
        else:
            return super().to_representation(instance)


class ProfileUserUpdateSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "username", "avatar", "full_name"]
        extra_kwargs = {
            "email": {
                "required": False,
            },
            "username": {
                "required": False,
            }
        }

    def update(self, instance, validated_data):
        instance.email = validated_data.get("email", instance.email)
        instance.username = validated_data.get("username", instance.username)
        instance.full_name = validated_data.get("full_name", instance.full_name)

        avatar = validated_data.get("avatar")
        if avatar:
            instance.avatar = avatar

        instance.save()

        return super().update(instance, validated_data)
