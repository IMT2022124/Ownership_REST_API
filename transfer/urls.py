from django.urls import path
from .views import TransferFileView, RevokeFileView, FileUploadView

urlpatterns = [
    path('upload/', FileUploadView.as_view(), name='upload-file'),
    path('transfer/', TransferFileView.as_view(), name='transfer-file'),
    path('revoke/', RevokeFileView.as_view(), name='revoke-file'),
]
