from rest_framework import serializers
from Website.models import User

class WebsiteSerializer(serializers.Serializer):
	id = serializers.IntegerField(read_only=True)
	username = serializers.CharField(style={'base_template': 'textarea.html'})
	isAdmin = serializers.BooleanField(required=False)

	def create(self, validated_data):
		return User.objects.create(**validated_data)

	def update(self, instance, validated_data):
		instance.username = validated_data.get('username', instance.username)
		instance.isAdmin = validated_data.get('isAdmin', instance.isAdmin)
		instance.save()
		return instance