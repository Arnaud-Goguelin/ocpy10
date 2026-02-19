from datetime import date, datetime

from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    age = serializers.SerializerMethodField(read_only=True)
    password = serializers.CharField(write_only=True, required=False, style={"input_type": "password"})

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password",
            "date_of_birth",
            "consent",
            "age",
        ]

    @staticmethod
    def get_age(obj: User) -> int | None:
        """Calculate age from date of birth"""
        if obj.date_of_birth:
            return User.calculate_age(obj.date_of_birth)
        return None

    @staticmethod
    def validate_date_of_birth(value: datetime) -> datetime:
        """Ensure date of birth is not in the future"""
        # reminder, with DRF a method name validate_{field_name} is automatically called
        if value and value > date.today():
            raise serializers.ValidationError("Date of birth cannot be in the future.")
        return value

    def validate_consent(self, value: bool) -> bool:
        """Ensure consent cannot be True if user is under 15 years old"""
        if not value:
            return value

        # Determine the date_of_birth to check
        date_of_birth = self.initial_data.get("date_of_birth")

        # If date_of_birth is not being updated, use existing value
        if not date_of_birth and self.instance:
            date_of_birth = self.instance.date_of_birth

        # if date of birth comes from initial data, it is a string, need to convert it to datetime
        if isinstance(date_of_birth, str):
            date_of_birth = date.fromisoformat(date_of_birth)

        age = User.calculate_age(date_of_birth)

        if age < 15:
            value = False

        return value

    def create(self, validated_data):
        # hass password
        # and ensure it is present to create a User object
        password = validated_data.pop("password", None)
        if not password:
            raise serializers.ValidationError("Password is required.")

        return User.objects.create_user(password=password, **validated_data)

    def update(self, instance: User, validated_data):
        # hash password
        password = validated_data.pop("password", None)
        if password:
            instance.set_password(password)

        # Update other fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance


class GDPRExportSerializer(UserSerializer):
    """Serializer for GDPR data export - extends UserSerializer with additional data"""

    class Meta(UserSerializer.Meta):
        fields = UserSerializer.Meta.fields + [
            "id",
            "first_name",
            "last_name",
            "date_joined",
            "last_login",
        ]
