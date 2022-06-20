from django.db.models import fields
from rest_framework import serializers
from .models import user

class userSerializer(serializers.ModelSerializer):
	class Meta:
		model = user
		fields = ('name', 'phone_number', 'gmail', 'address')
