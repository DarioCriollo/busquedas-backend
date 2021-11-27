from rest_framework import serializers
from apps.inquiries.models import Inquiries

class InquiriesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Inquiries
        fields = ('id', 'word', 'number_searches', 'number_results')