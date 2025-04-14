from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import AdvertisementCategory
from .serializers import AdvertisementCategorySerializer

class AdvertisementCategoryAPIView(APIView):
    # GET: Retrieve all advertisement categories
    def get(self, request):
        categories = AdvertisementCategory.objects.all()
        serializer = AdvertisementCategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # POST: Create a new advertisement category
    def post(self, request):
        serializer = AdvertisementCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AdvertisementCategoryDetailAPIView(APIView):
    # GET: Retrieve a single advertisement category by ID
    def get(self, request, pk):
        try:
            category = AdvertisementCategory.objects.get(pk=pk)
        except AdvertisementCategory.DoesNotExist:
            return Response({'error': 'AdvertisementCategory not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = AdvertisementCategorySerializer(category)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # DELETE: Delete an advertisement category by ID
    def delete(self, request, pk):
        try:
            category = AdvertisementCategory.objects.get(pk=pk)
        except AdvertisementCategory.DoesNotExist:
            return Response({'error': 'AdvertisementCategory not found'}, status=status.HTTP_404_NOT_FOUND)

        category.delete()
        return Response({'message': 'AdvertisementCategory deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

from rest_framework import viewsets
from .models import Advertisement
from .serializers import AdvertisementSerializer

class AdvertisementViewSet(viewsets.ModelViewSet):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer

    # GET API: List all advertisements
    def list(self, request, *args, **kwargs):
        queryset = Advertisement.objects.all()
        serializer = AdvertisementSerializer(queryset, many=True)
        return Response(serializer.data)

    # POST API: Create a new advertisement
    def create(self, request, *args, **kwargs):
        serializer = AdvertisementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    # DELETE API: Delete an advertisement
    def destroy(self, request, *args, **kwargs):
        advertisement = self.get_object()
        advertisement.delete()
        return Response(status=204)

# views.py
from rest_framework.views import APIView
from .serializers import AdvertisementSerializer

class AdvertisementByCategoryView(APIView):
    def get(self, request, category_id):
        # Check if the category exists
        try:
            category = AdvertisementCategory.objects.get(id=category_id)
        except AdvertisementCategory.DoesNotExist:
            return Response({"error": "Category not found"}, status=status.HTTP_404_NOT_FOUND)

        # Filter advertisements by category and is_active
        advertisements = Advertisement.objects.filter(category=category, is_active=True)
        serializer = AdvertisementSerializer(advertisements, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


