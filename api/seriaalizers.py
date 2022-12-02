from rest_framework import serializers
class ConfSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    Title = serializers.CharField(max_length=None, min_length=None, allow_blank=False, trim_whitespace=True)
    ConfDate = serializers.CharField(max_length=None, min_length=None, allow_blank=False, trim_whitespace=True)
    ConfTag = serializers.CharField(max_length=None, min_length=None, allow_blank=False, trim_whitespace=True)