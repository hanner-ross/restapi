from rest_framework import serializers
from usuarios.models import Usuarios, Tableros, Ideas

class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = ('id', 'user', 'password', 'name', 'last_name','id_number', 'picture')

class TablerosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tableros
        fields = ('id', 'table_owner', 'table_name', 'table_privacy')

class IdeasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ideas
        fields = ('id', 'user_name', 'table_name', 'thing')