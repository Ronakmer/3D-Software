from django.db.models import fields
from rest_framework import serializers
from .models import user

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = user
		fields = ('name', 'username','phone_number', 'gmail', 'address','password')