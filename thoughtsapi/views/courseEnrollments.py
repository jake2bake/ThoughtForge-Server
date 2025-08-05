# readings/courseenrollment.py

from rest_framework import viewsets, serializers
from rest_framework.response import Response
from rest_framework import status
from thoughtsapi.models import CourseEnrollment

class CourseEnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseEnrollment
        fields = '__all__'

class CourseEnrollmentViewSet(viewsets.ViewSet):
    def list(self, request):
        enrollments = CourseEnrollment.objects.all()
        serializer = CourseEnrollmentSerializer(enrollments, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            enrollment = CourseEnrollment.objects.get(pk=pk)
            serializer = CourseEnrollmentSerializer(enrollment)
            return Response(serializer.data)
        except CourseEnrollment.DoesNotExist:
            return Response({'error': 'Course enrollment not found'}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        serializer = CourseEnrollmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            enrollment = CourseEnrollment.objects.get(pk=pk)
        except CourseEnrollment.DoesNotExist:
            return Response({'error': 'Course enrollment not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = CourseEnrollmentSerializer(enrollment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            enrollment = CourseEnrollment.objects.get(pk=pk)
            enrollment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except CourseEnrollment.DoesNotExist:
            return Response({'error': 'Course enrollment not found'}, status=status.HTTP_404_NOT_FOUND)
