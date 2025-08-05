# readings/readingassignment.py

from rest_framework import viewsets, serializers
from rest_framework.response import Response
from rest_framework import status
from thoughtsapi.models import ReadingAssignment

class ReadingAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReadingAssignment
        fields = '__all__'

class ReadingAssignmentViewSet(viewsets.ViewSet):
    def list(self, request):
        assignments = ReadingAssignment.objects.all()
        serializer = ReadingAssignmentSerializer(assignments, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            assignment = ReadingAssignment.objects.get(pk=pk)
            serializer = ReadingAssignmentSerializer(assignment)
            return Response(serializer.data)
        except ReadingAssignment.DoesNotExist:
            return Response({'error': 'ReadingAssignment not found'}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        serializer = ReadingAssignmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            assignment = ReadingAssignment.objects.get(pk=pk)
        except ReadingAssignment.DoesNotExist:
            return Response({'error': 'ReadingAssignment not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = ReadingAssignmentSerializer(assignment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            assignment = ReadingAssignment.objects.get(pk=pk)
            assignment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ReadingAssignment.DoesNotExist:
            return Response({'error': 'ReadingAssignment not found'}, status=status.HTTP_404_NOT_FOUND)
