from candidate_api.models import Candidate
from candidate_api.serializers import CandidateSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class CandidateList(APIView):
    """
    List all candidates, or create a new candidate.
    """
    def get(self, request, format=None):
        candidates = Candidate.objects.all()
        if request.query_params and 'short' in request.query_params:
            result = [candidate.id for candidate in candidates]
            return Response(result)

        serializer = CandidateSerializer(candidates, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CandidateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
class CandidateDetail(APIView):
    """
    Retrieve, update or delete a candidate instance.
    """
    def get_object(self, pk):
        try:
            return Candidate.objects.get(pk=pk)
        except Candidate.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        candidate = self.get_object(pk)
        serializer = CandidateSerializer(candidate)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        candidate = self.get_object(pk)
        serializer = CandidateSerializer(candidate, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        candidate = self.get_object(pk)
        candidate.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)