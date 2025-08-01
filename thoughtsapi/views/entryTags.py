from rest_framework import viewsets, status, serializers
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from thoughtsapi.models import EntryTag, Entry, Tag

class EntryTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntryTag
        fields = '__all__'

class EntryTagViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        entry_tags = EntryTag.objects.all()
        serializer = EntryTagSerializer(entry_tags, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            entry_tag = EntryTag.objects.get(pk=pk)
            serializer = EntryTagSerializer(entry_tag)
            return Response(serializer.data)
        except EntryTag.DoesNotExist:
            return Response({'message': 'EntryTag not found'}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        serializer = EntryTagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            entry_tag = EntryTag.objects.get(pk=pk)
            serializer = EntryTagSerializer(entry_tag, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except EntryTag.DoesNotExist:
            return Response({'message': 'EntryTag not found'}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        try:
            entry_tag = EntryTag.objects.get(pk=pk)
            entry_tag.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except EntryTag.DoesNotExist:
            return Response({'message': 'EntryTag not found'}, status=status.HTTP_404_NOT_FOUND)
