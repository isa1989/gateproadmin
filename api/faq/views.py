from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from faq.models import FAQ
from .serializers import FAQSerializer


class FAQListView(ListAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer


class FAQDetailView(RetrieveAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer
    lookup_field = "id"

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        return Response(data, status=status.HTTP_200_OK)


class MarkFAQHelpful(UpdateAPIView):
    permission_classes = [AllowAny]
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer
    lookup_url_kwarg = "id"

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.mark_as_helpful()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(
            {"message": "FAQ marked as helpful."}, status=status.HTTP_200_OK
        )


class MarkFAQNotHelpful(UpdateAPIView):
    permission_classes = [AllowAny]
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer
    lookup_url_kwarg = "id"

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.mark_as_not_helpful()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(
            {"message": "FAQ marked as not helpful."}, status=status.HTTP_200_OK
        )
