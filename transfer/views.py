from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, generics
from .models import File, TransferHistory
from django.contrib.auth.models import User
from .serializers import FileSerializer, TransferHistorySerializer
from django.shortcuts import get_object_or_404
from rest_framework.parsers import MultiPartParser, FormParser

class TransferFileView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        file_id = request.data.get("file_id")
        to_user_id = request.data.get("to_user_id")

        if not file_id or not to_user_id:
            return Response({"error": "file_id and to_user_id are required."}, status=400)

        file = get_object_or_404(File, id=file_id)
        to_user = get_object_or_404(User, id=to_user_id)

        # Only current owner can transfer
        if file.owner != request.user:
            return Response({"error": "You are not the owner of this file."}, status=403)

        # Update file owner
        from_user = file.owner
        file.owner = to_user
        file.save()

        # Log transfer
        TransferHistory.objects.create(
            file=file,
            from_user=from_user,
            to_user=to_user,
            action="TRANSFER"
        )

        return Response({"message": "File transferred successfully."}, status=200)

class RevokeFileView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        file_id = request.data.get("file_id")
        file = get_object_or_404(File, id=file_id)

        # Only original owner can revoke
        if file.original_owner != request.user:
            return Response({"error": "You are not the original owner of this file."}, status=403)

        # Update file owner back to original owner
        from_user = file.owner
        file.owner = file.original_owner
        file.save()

        # Log revoke
        TransferHistory.objects.create(
            file=file,
            from_user=from_user,
            to_user=file.original_owner,
            action="REVOKE"
        )

        return Response({"message": "File revoked successfully."}, status=200)

class FileUploadView(generics.CreateAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user, original_owner=self.request.user)
