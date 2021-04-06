from rest_framework import serializers
from django.utils.timezone import now
from .models import UserProfile, encuesta_1

class encuestaSerializer(serializers.ModelSerializer):
    """Serializa un campo para probar nuestra APIView"""
    
    class Meta:
        
        model = encuesta_1
        fields = '__all__'

class usuarioSerializer(serializers.ModelSerializer):
    """Serializa un campo para probar nuestra APIView"""
    
    class Meta:
        
        model = UserProfile
        fields = ('email', 'name','is_active','is_staff')

