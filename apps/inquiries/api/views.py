from rest_framework.views import APIView
from apps.inquiries.models import Inquiries
from rest_framework.response import Response
from apps.inquiries.api.serializers import InquiriesSerializers

class ListInquiriesApiView(APIView):
    def get(self, request):
        inquiries = Inquiries.objects.all()
        inquiries_json = InquiriesSerializers(inquiries, many=True)
        return Response(inquiries_json.data)