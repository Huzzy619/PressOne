from rest_framework import serializers

from new_app.models import Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ["id", "name", "created_at", "updated_at"]
