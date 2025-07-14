from rest_framework import serializers
from .models import File, TransferHistory

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['id', 'name', 'file', 'owner', 'original_owner', 'created_at']
        read_only_fields = ['owner', 'original_owner', 'created_at']

class TransferHistorySerializer(serializers.ModelSerializer):
    file = serializers.StringRelatedField()
    from_user = serializers.StringRelatedField()
    to_user = serializers.StringRelatedField()

    class Meta:
        model = TransferHistory
        fields = ['id', 'file', 'from_user', 'to_user', 'action', 'timestamp']
