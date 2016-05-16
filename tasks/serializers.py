from rest_framework import serializers
from tasks.models import Cards


class CardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cards
        fields = ('title', 'comments', 'description')

    def create(self, validated_data):
        """
        Create and return a new `Cards` instance, given data.
        """
        return Cards.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Cards` instance, given data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.comments = validated_data.get('comments', instance.comments)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance
