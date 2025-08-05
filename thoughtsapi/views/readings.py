# readings/reading.py

from rest_framework import viewsets, serializers
from rest_framework.response import Response
from rest_framework import status
from thoughtsapi.models import Reading

class ReadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reading
        fields = '__all__'

class ReadingViewSet(viewsets.ViewSet):
    def list(self, request):
        readings = Reading.objects.all()
        serializer = ReadingSerializer(readings, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            reading = Reading.objects.get(pk=pk)
            serializer = ReadingSerializer(reading)
            return Response(serializer.data)
        except Reading.DoesNotExist:
            return Response({'error': 'Reading not found'}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        serializer = ReadingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            reading = Reading.objects.get(pk=pk)
        except Reading.DoesNotExist:
            return Response({'error': 'Reading not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = ReadingSerializer(reading, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            reading = Reading.objects.get(pk=pk)
            reading.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Reading.DoesNotExist:
            return Response({'error': 'Reading not found'}, status=status.HTTP_404_NOT_FOUND)
