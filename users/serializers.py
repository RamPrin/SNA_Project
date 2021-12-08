from rest_framework import serializers

from .models import CustomUser


class UserSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ('url', 'username', 'password', 'date_joined', 'is_superuser', 'is_staff')
        read_only_fields = ('is_superuser', 'is_staff', 'date_joined')

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
        )

        return user
