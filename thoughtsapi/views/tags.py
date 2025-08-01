from rest_framework import viewsets, status, serializers
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from thoughtsapi.models import Tag

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class TagViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def list(self, request):
        tags = Tag.objects.all()
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            tag = Tag.objects.get(pk=pk)
            serializer = TagSerializer(tag)
            return Response(serializer.data)
        except Tag.DoesNotExist:
            return Response({'message': 'Tag not found'}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        serializer = TagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            tag = Tag.objects.get(pk=pk)
            serializer = TagSerializer(tag, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Tag.DoesNotExist:
            return Response({'message': 'Tag not found'}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        try:
            tag = Tag.objects.get(pk=pk)
            tag.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Tag.DoesNotExist:
            return Response({'message': 'Tag not found'}, status=status.HTTP_404_NOT_FOUND)
