from rest_framework import serializers
from imageprocessingrequests.models import ImageProcessingRequest

class ImageProcessingRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageProcessingRequest
        fields = ('id', 'patientid', 'jobtype', 'jobstatus')
