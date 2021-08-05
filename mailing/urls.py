from django.urls import path
from .views import MailingCreateView, MailingUpdateView, MailingDeleteView, MailingListView, MailingDetailView

urlpatterns = [
    path('', MailingListView.as_view(), name='mailing_list'),
    path('<int:pk>', MailingDetailView.as_view(), name='mailing_detail'),
    path('add/', MailingCreateView.as_view(), name='mailing_create'),
    path('<int:pk>/update/', MailingUpdateView.as_view(), name='mailing_update'),
    path('<int:pk>/delete/', MailingDeleteView.as_view(), name='mailing_delete'),
]