from rest_framework import serializers
from .models import multi, jobs, Tag
from datetime import datetime
from django.utils.timesince import timesince


class TagSerializer(serializers.ModelSerializer):
    # # job = multiSerializer(many=True, read_only=True)
    # id = serializers.ReadOnlyField(source='jobs.id')
    # name = serializers.ReadOnlyField(source='member.name')

    class Meta:
        model = Tag
        fields = "__all__"


class multiSerializer(serializers.ModelSerializer):
    time_delta_pub = serializers.SerializerMethodField()
    # job = jobSerializer(read_only=True)
    tags = TagSerializer(read_only=True, many=True)

    class Meta:
        model = multi
        fields = "__all__"

    def get_time_delta_pub(self, object):
        publicatioon_date = object.publicatioon_date
        now = datetime.now()
        time_deita = timesince(publicatioon_date, now)
        return time_deita


class jobSerializer(serializers.ModelSerializer):
    # job = multiSerializer(many=True, read_only=True)

    class Meta:
        model = jobs
        fields = "__all__"
