from django.urls import path
from apps.inquiries.api import views


urlpatterns = [
    path('inquiries/', views.ListInquiriesApiView.as_view()),
    path('inquiries/<pk>', views.DetailInquiriesApiView.as_view()),
]