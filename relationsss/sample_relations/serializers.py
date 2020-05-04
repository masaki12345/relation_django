from rest_framework import serializers
from .models import multi, jobs


class jobSerializer(serializers.ModelSerializer):

    class Meta:
        model = jobs
        fields = "__all__"


class multiSerializer(serializers.ModelSerializer):
    job = jobSerializer()

    class Meta:
        model = multi
        fields = "__all__"

