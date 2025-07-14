from django.db import models
from django.contrib.auth.models import User

class File(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='uploads/')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned_files')
    original_owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='originally_owned_files')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class TransferHistory(models.Model):
    ACTION_CHOICES = (
        ('TRANSFER', 'Transfer'),
        ('REVOKE', 'Revoke'),
    )
    file = models.ForeignKey(File, on_delete=models.CASCADE)
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transfers_made')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transfers_received')
    action = models.CharField(max_length=10, choices=ACTION_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.action} of {self.file.name}"
