from rest_framework.views import APIView
from apps.inquiries.models import Inquiries
from rest_framework.response import Response
from apps.inquiries.api.serializers import InquiriesSerializers
from django.http import Http404

class ListInquiriesApiView(APIView):
    def get(self, request):
        inquiries = Inquiries.objects.all()
        inquiries_json = InquiriesSerializers(inquiries, many=True)
        return Response(inquiries_json.data)

    def post(self, request):
        inquiries_json = InquiriesSerializers(data=request.data)
        if inquiries_json.is_valid():
            inquiries_json.save()
            return Response(inquiries_json.data, status=201)
        return Response(inquiries_json.data, status=400)

class DetailInquiriesApiView(APIView):
    def get_object(self, pk):
        try:
              return Inquiries.objects.get(pk)
        except Inquiries.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        try:
            inquiries = Inquiries.objects.get(pk=pk)
            inquiries_json = InquiriesSerializers(inquiries)
            return Response(inquiries_json.data)
        except Inquiries.DoesNotExist:
            raise Http404
    
    def put(self, request, pk):
        try:
            inquiries = Inquiries.objects.get(pk=pk)
            inquiries_json = InquiriesSerializers(inquiries, data=request.data)
            if inquiries_json.is_valid:
                inquiries_json.save()
                return Response(inquiries_json.data)
            return Response(inquiries_json.data, status=400)
        except Inquiries.DoesNotExist:
            raise Http404

    def delete(self, request, pk):
        try:
            inquiries = Inquiries.objects.get(pk=pk)
            inquiries.delete()
            return Response(status=204)
        except Inquiries.DoesNotExist:
            raise Http404
