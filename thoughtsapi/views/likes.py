from rest_framework import viewsets, serializers, status
from rest_framework.response import Response
from thoughtsapi.models import Like, Entry


class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = '__all__'

# Serializer
class LikeSerializer(serializers.ModelSerializer):
    entry_details = EntrySerializer(source='entry', many=False, read_only=True)

    class Meta:
        model = Like
        fields = ['id', 'user', 'entry', 'created_at', 'entry_details']

# ViewSet
class LikeViewSet(viewsets.ViewSet):
    def list(self, request):
        likes = Like.objects.all()
        serializer = LikeSerializer(likes, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            like = Like.objects.get(pk=pk)
            serializer = LikeSerializer(like)
            return Response(serializer.data)
        except Like.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        serializer = LikeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            like = Like.objects.get(pk=pk)
        except Like.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = LikeSerializer(like, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            like = Like.objects.get(pk=pk)
            like.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Like.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
