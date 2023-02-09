from rest_framework import serializers
from hige.models import ItemsListTemplate, ItemsListTemplateItem, ItemsList, ItemsListItem

class ItemsListTemplateItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemsListTemplateItem 
        fields = ['name']

class ItemsListTemplateSerializer(serializers.HyperlinkedModelSerializer):
    user_id = serializers.CharField(read_only=True)
    items = ItemsListTemplateItemSerializer(many=True, read_only=True)
    description = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = ItemsListTemplate
        fields = ['id', 'name', 'description', 'user_id', 'items']
        read_only_fields = ['id']

class ItemsListItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemsListItem
        fields = ['id', 'checked', 'name']
        read_only_fields = ['id']

class ItemsListSerializer(serializers.ModelSerializer):
    items = ItemsListItemSerializer(many=True, read_only=True)

    class Meta:
        model = ItemsList
        fields = ['id', 'name', 'items', 'is_active']
        read_only_fields = ['id']