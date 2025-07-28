from rest_framework import serializers
from .models import User, Product
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'password', 'first_name','last_name', 'date_joined')
        read_only_fields = ['id',  'date_joined']
        extrat_kwargs ={
            'password' : {'write_only': True}
            }
    
    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['emil'],
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user
class UserRegisterationSerializer(serializers.ModelSerializer):
    """
    **Objective**: Handle user registration with password validation
    **Key Concepts**:
    - write_only: Password field won't be returned in API responses
    - create() method: Custom logic for creating user with hashed password
    """
    password = serializers.CharField(write_only = True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'first_name','last_name']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class ProductSerializer(serializers.ModelSerializer):
    """
    **Objective**: Convert Product model instances to JSON for API responses
    **Key Concepts**:
    - ModelSerializer: Automatically handles model field serialization
    - Meta class: Configuration for the serializer
    """
    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']
    
    def validate_specifications(self, value):
        """
        **Objective**: Handle specifications from form-data
        **Key Concepts**:
        - value: Can be dict (from JSON) or string (from form-data)
        - json.loads(): Convert string to dict if needed
        """

        import json 
        if isinstance(value, str):
            try:
                return json.loads(value)
            except json.JSONDecodeError:
                raise serializers.ValidationError("Invalid JSON format fot specifications")
        return value