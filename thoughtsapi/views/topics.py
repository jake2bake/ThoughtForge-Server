from rest_framework import viewsets, status, serializers
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from thoughtsapi.models import Topic

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'

class TopicViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def list(self, request):
        topics = Topic.objects.all()
        serializer = TopicSerializer(topics, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            topic = Topic.objects.get(pk=pk)
            serializer = TopicSerializer(topic)
            return Response(serializer.data)
        except Topic.DoesNotExist:
            return Response({'message': 'Topic not found'}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        serializer = TopicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            topic = Topic.objects.get(pk=pk)
            serializer = TopicSerializer(topic, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Topic.DoesNotExist:
            return Response({'message': 'Topic not found'}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        try:
            topic = Topic.objects.get(pk=pk)
            topic.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Topic.DoesNotExist:
            return Response({'message': 'Topic not found'}, status=status.HTTP_404_NOT_FOUND)
