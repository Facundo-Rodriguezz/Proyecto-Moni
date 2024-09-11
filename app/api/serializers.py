from rest_framework import serializers
from .models import Prestamo, CustomUsers
from .models import UsuarioAd

#creo la clase PrestamoSerializer para que me devuelva los datos
class PrestamoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prestamo
        fields = ['id','dni', 'nombre_apellido', 'genero', 'email', 'monto_solicitado', 'aprobado']

#creo la clase CustomUsersSerializer para que me devuelva los datos
class CustomUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUsers
        fields = [ 'email', 'password', 'is_admin']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioAd
        fields = ['username', 'email', 'full_name', 'phone_number', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UsuarioAd.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            full_name=validated_data['full_name'],
            phone_number=validated_data['phone_number'],
            password=validated_data['password']
        )
        return user