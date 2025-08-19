from rest_framework import viewsets, serializers, status
from rest_framework.response import Response
from thoughtsapi.models import Share, Entry, Reading, Course

class ReadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reading
        fields = ['id', 'title', 'author']

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = '__all__'

# Serializer
class ShareSerializer(serializers.ModelSerializer):
    entry_details = EntrySerializer(source='entry', many=False, read_only=True)
    course_details = CourseSerializer(source='course', many=False, read_only=True)
    reading_details = ReadingSerializer(source='reading', many=False, read_only=True)
    class Meta:
        model = Share
        fields = ['id', 'user', 'entry', 'shared_to', 'course', 'entry_details', 'course_details', 'reading_details', 'reading', 'created_at']

# ViewSet
class ShareViewSet(viewsets.ViewSet):
    def list(self, request):
        shares = Share.objects.all()
        serializer = ShareSerializer(shares, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            share = Share.objects.get(pk=pk)
            serializer = ShareSerializer(share)
            return Response(serializer.data)
        except Share.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        serializer = ShareSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            share = Share.objects.get(pk=pk)
        except Share.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ShareSerializer(share, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            share = Share.objects.get(pk=pk)
            share.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Share.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
