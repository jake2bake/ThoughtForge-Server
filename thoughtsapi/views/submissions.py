from rest_framework import viewsets, serializers, status
from rest_framework.response import Response
from thoughtsapi.models import Submission

# Serializer
class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = ['id', 'title', 'reflection', 'user', 'reading', 'submitted_at', 'grade', 'feedback']
        read_only_fields = ['submitted_att']
        extra_kwargs = {
            'grade': {'required': False},
            'feedback': {'required': False}
        }


# ViewSet
class SubmissionViewSet(viewsets.ViewSet):
    def list(self, request):
        submissions = Submission.objects.all()
        serializer = SubmissionSerializer(submissions, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            submission = Submission.objects.get(pk=pk)
            serializer = SubmissionSerializer(submission)
            return Response(serializer.data)
        except Submission.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        serializer = SubmissionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            submission = Submission.objects.get(pk=pk)
        except Submission.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = SubmissionSerializer(submission, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            submission = Submission.objects.get(pk=pk)
            submission.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Submission.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
