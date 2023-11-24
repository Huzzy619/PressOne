from uuid import UUID

from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from new_app.models import Item
from new_app.serializers import ItemSerializer


class ItemDetailView(APIView):
    serializer_class = ItemSerializer

    def get(self, request: Request, item_id: UUID):
        """
        Get an item by its ID.

        Args:
            request (Request): The HTTP request object.
            item_id (UUID): The ID of the item to retrieve.

        Returns:
            Response: The HTTP response object containing the serialized item data.

        Raises:
            Item.DoesNotExist: If the item with the given ID does not exist.
        """
        try:
            item = Item.objects.get(id=item_id)
        except Item.DoesNotExist:
            return Response(
                data={"error": f"Item with {item_id} not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = ItemSerializer(instance=item)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class ItemCreateView(APIView):
    serializer_class = ItemSerializer

    def post(self, request: Request):
        """
        Handle POST requests.

        Parameters:
            - request (Request): The HTTP request object containing the request data.

        Returns:
            - Response: The HTTP response object containing the serialized data and the status code.
        """
        serializer = ItemSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
