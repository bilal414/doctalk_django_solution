from rest_framework import serializers
from apps.console.doctalk.models import Profile, Food


class FoodSerializer(serializers.ModelSerializer):
    group_display = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Food

    @staticmethod
    def get_group_display(obj):
        return obj.get_group_display()


class ProfileSerializer(serializers.ModelSerializer):
    fav_food = FoodSerializer(read_only=True)
    dob_display = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = "__all__"

    @staticmethod
    def get_dob_display(obj):
        date_time = obj.dob.strftime("%b %d %Y - %I:%M%p")
        return date_time
