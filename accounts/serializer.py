from rest_framework import serializers
from . import services


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    username = serializers.CharField()
    email = serializers.CharField()
    password = serializers.CharField(write_only=True)
    birthdate = serializers.DateField(required=False)
    createdAt = serializers.DateField(required=False)
    lastUpdate = serializers.DateTimeField(required=False)
    profilePic = serializers.ImageField(required=False)
    teacher = serializers.BooleanField(required=False)

    def to_internal_value(self, data):
        data = super().to_internal_value(data)

        return services.UserDataClass(**data)


class EditSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=False, allow_null=True)
    username = serializers.CharField(required=False, allow_null=True)
    email = serializers.CharField(required=False, allow_null=True)
    password = serializers.CharField(write_only=True, required=False, allow_null=True)
    birthdate = serializers.DateField(required=False, allow_null=True)
    createdAt = serializers.DateField(required=False, allow_null=True)
    lastUpdate = serializers.DateTimeField(required=False, allow_null=True)
    profilePic = serializers.ImageField(required=False, allow_null=True)
    teacher = serializers.BooleanField(required=False, default=False)

    def to_internal_value(self, data):
        data = super().to_internal_value(data)

        return services.UserDataClass(**data)