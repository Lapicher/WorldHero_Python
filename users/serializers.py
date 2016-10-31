from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework import serializers
from django.core.exceptions import ValidationError



class UserSerializer(serializers.Serializer):

    id = serializers.ReadOnlyField()
    first_name = serializers.CharField()  # la variable debe tener mismo nombre del campo
    last_name = serializers.CharField()
    username = serializers.CharField()
    password = serializers.CharField()
    email = serializers.CharField()

    def create(self, validated_data):
        instance = User()
        return self.update(instance, validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name')
        instance.last_name = validated_data.get('last_name')
        instance.username = validated_data.get('username')
        instance.password = make_password(validated_data.get('password'))
        instance.email = validated_data.get('email')
        instance.save()
        return instance

    def validate_username(self, username):
        # validacion para que pueda modificar el administrador y el usuario, pero validando que no exista el usuario.
        if (self.instance is None or self.instance.username != username) \
                and User.objects.filter(username=username).exists():
            raise ValidationError(_("El nombre de usuario {0} ya está siendo utilizado").format(username))
        return username

    def validate_email(self, email):
        if (self.instance is None or self.instance.email != email) and User.objects.filter(email=email).exists():
            raise ValidationError(_("El e-mail {0} ya está siendo utilizado").format(email))
        return email.lower()

    def validate(self, attrs):
        return attrs


