from django.db.models import fields
from rest_framework import serializers
from .models import signup

class signupSerializer(serializers.ModelSerializer):
	class Meta:
		model = signup
		fields = ('name', 'phone_number', 'gmail', 'address')
