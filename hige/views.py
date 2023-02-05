from hige.serializers import ItemsListTemplateSerializer, ItemsListTemplateItemSerializer, ItemsListSerializer, ItemsListItemSerializer
from hige.models import ItemsListTemplate, ItemsListTemplateItem, ItemsList, ItemsListItem

from rest_framework import permissions, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

class ItemListTemplateViewSet(viewsets.ModelViewSet):
    serializer_class = ItemsListTemplateSerializer 
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return ItemsListTemplate.objects.filter(user_id=self.request.user).order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)
        

class ItemListTemplateItemViewSet(viewsets.ModelViewSet):
    serializer_class = ItemsListTemplateItemSerializer 
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return ItemsListTemplateItem.objects.filter(items_list_id=self.kwargs["items_list_template_id"])

    def perform_create(self, serializer):
        serializer.save(items_list_id=self.kwargs["items_list_template_id"])

    def get_serializer(self, *args, **kwargs):
        if isinstance(kwargs.get("data", {}), list):
            kwargs["many"] = True

        return super(ItemListTemplateItemViewSet, self).get_serializer(*args, **kwargs)
    
    @action(methods=['put'], detail=False)
    def replace(self, request, *args, **kwargs):
        self.get_queryset().delete()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data)

class ItemListViewSet(viewsets.ModelViewSet):
    serializer_class = ItemsListSerializer 
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return ItemsList.objects.filter(user_id=self.request.user, is_active=True).order_by('-created_at')

    @action(methods=['post'], detail=False)
    def create_from_template(self, request, *args, **kwargs):
        template_id = kwargs["template_id"]
        template = ItemsListTemplate.objects.prefetch_related("items").get(id=template_id, user_id=self.request.user)

        newList = ItemsList(name="List", user_id=self.request.user, is_active=True)
        newList.save()
        
        templateItems = template.items.all()

        newItems = []
        for item in templateItems:
            newItem = ItemsListItem(active_item_list=newList, name=item.name, checked=False)
            newItems.append(newItem)

        ItemsListItem.objects.bulk_create(newItems)

        serializer = self.get_serializer(newList)
        return Response(serializer.data)

class ItemsListItemViewSet(viewsets.ModelViewSet):
    serializer_class = ItemsListItemSerializer 
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return ItemsListItem.objects.filter(active_item_list_id=self.kwargs["items_list_id"], active_item_list__user_id=self.request.user)