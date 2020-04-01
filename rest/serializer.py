from rest_framework import serializers

class UserSerializer(serializers.Serializer):
        username = serializers.CharField(max_length=10)
        now_lecture = serializers.CharField(max_length=20)
        now_room = serializers.CharField(max_length=10)
        now_room_beacon_major = serializers.CharField(max_length=10)
        now_room_beacon_minor = serializers.CharField(max_length=10)