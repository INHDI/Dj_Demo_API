from rest_framework import serializers
from home.models import Klee

class KleeSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    title = serializers.CharField(max_length=200)
    code = serializers.CharField()
    date = serializers.DateTimeField()

    def create(self,validate_data):
        return  Klee.objects.create(**validate_data)
    def update(self,instance,validate_data):
        instance.name = validate_data.get('name',instance.name)
        instance.title =validate_data.get('title',instance.title)
        instance.code =validate_data.get('code',instance.code)
        instance.date =validate_data.get('date',instance.date)
        instance.save()
        return instance