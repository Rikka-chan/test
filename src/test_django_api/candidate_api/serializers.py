from rest_framework import serializers
from candidate_api.models import Candidate


class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ('photo_url',
                  'last_name',
                  'first_name',
                  'birthday',
                  'address',
                  'phone_number',
                  'email',
                  'description',
                  'salary',
                  'id')