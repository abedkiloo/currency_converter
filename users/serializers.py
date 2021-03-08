from rest_framework import serializers

from users.models import Account


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = Account
        fields = (
            "id",
            "email",
            "password",
            "password2",
            "user_name",
            "first_name",
            "last_name",
            "is_superuser",
        )
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def save(self, *args, **kwargs):
        user = Account(
            email=self.validated_data["email"],
            user_name=self.validated_data["user_name"],
        )

        password = self.validated_data["password"]
        password2 = self.validated_data["password2"]
        if password != password2:
            raise serializers.ValidationError({"password": "password must match"})

        user.set_password(password)
        user.save()
        return user
