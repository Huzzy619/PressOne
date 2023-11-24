from django.urls import path

from new_app.views import ItemCreateView, ItemDetailView

urlpatterns = [
    path("items/create", ItemCreateView.as_view(), name="item-create"),
    path("items/<uuid:item_id>", ItemDetailView.as_view(), name="item-detail"),
]
