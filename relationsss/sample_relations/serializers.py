from rest_framework import serializers
from .models import multi, jobs


class multiSerializer(serializers.ModelSerializer):
    # job = jobSerializer(read_only=True)

    class Meta:
        model = multi
        fields = "__all__"


class jobSerializer(serializers.ModelSerializer):
    job = multiSerializer(many=True, read_only=True)

    class Meta:
        model = jobs
        fields = "__all__"
