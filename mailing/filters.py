from django_filters import FilterSet
from .models import Mailing


class MailingFilter(FilterSet):

    class Meta:
        model = Mailing
        fields = {
            'subject': ['icontains'],
            'body': ['icontains'],

        }



