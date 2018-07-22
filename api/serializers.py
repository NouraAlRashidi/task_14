from rest_framework import serializers
from restaurants.models import Restaurant

class APIListSerializer (serializers.ModelSerializer):
	class Meta:
		model = Restaurant
		fields = ['name','opening_time','closing_time',]