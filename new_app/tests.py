from uuid import uuid4

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from new_app.models import Item


class ItemDetailViewTest(APITestCase):
    def test_get_item_detail(self):
        item = Item.objects.create(name="Test Item")
        url = reverse("item-detail", kwargs={"item_id": str(item.id)})

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], str(item.id))
        self.assertEqual(response.data["name"], item.name)

    def test_get_item_detail_not_found(self):
        fake_id = str(uuid4())
        url = reverse("item-detail", kwargs={"item_id": fake_id})

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertIn("error", response.data)
        self.assertEqual(response.data["error"], f"Item with {fake_id} not found")


class ItemCreateViewTest(APITestCase):
    def setUp(self):
        self.url = reverse("item-create")

    def test_create_item(self):
        payload = {"name": "New Test Item"}
        response = self.client.post(self.url, payload, format="json")

        self.assertEqual(response.data["name"], payload.get("name"))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Item.objects.count(), 1)

    def test_create_item_invalid_payload(self):
        payload = {"name": ""}

        response = self.client.post(self.url, payload, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("name", response.data)
