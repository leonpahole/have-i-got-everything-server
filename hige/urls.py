from django.urls import path

from hige.views import ItemListTemplateViewSet, ItemListTemplateItemViewSet, ItemListViewSet, ItemsListItemViewSet 
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'templates', ItemListTemplateViewSet, basename="templates")
router.register(r'templates/(?P<items_list_template_id>\d+)/template_items', ItemListTemplateItemViewSet, basename="template_items")
router.register(r'lists', ItemListViewSet, basename="lists")
router.register(r'lists/(?P<items_list_id>\d+)/list_items', ItemsListItemViewSet, basename="list_items")

urlpatterns = [ 
    path('lists/create_from_template/<int:template_id>/', ItemListViewSet.as_view({'post': 'create_from_template'})),
    path('', include(router.urls)),
]

