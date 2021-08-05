from django.shortcuts import render
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Mailing
from .forms import MailingForm
from .filters import MailingFilter
# Create your views here.


class MailingCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Mailing
    template_name = 'mailing_create.html'
    context_object_name = 'mailing'
    permission_required = ('mailing.add_mailing',)
    form_class = MailingForm
    success_url = '/mailing/'


class MailingUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Mailing
    template_name = 'mailing_update.html'
    context_object_name = 'mailing'
    permission_required = ('mailing.add_mailing',)
    form_class = MailingForm
    success_url = '/mailing/'


class MailingDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Mailing
    template_name = 'mailing_detail.html'
    context_object_name = 'mailing'
    permission_required = ('mailing.add_mailing',)
    form_class = MailingForm


class MailingDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Mailing
    template_name = 'mailing_delete.html'
    context_object_name = 'mailing'
    permission_required = ('mailing.add_mailing',)
    form_class = MailingForm
    success_url = '/mailing/'


class MailingListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Mailing
    template_name = 'mailing_list.html'
    permission_required = ('mailing.add_mailing',)
    context_object_name = 'mailings'
    queryset = Mailing.objects.order_by('-id')
    paginate_by = 10

    def get_context_data(self, **kwargs):  # забираем отфильтрованные объекты переопределяя метод get_context_data у наследуемого класса (привет, полиморфизм, мы скучали!!!)
        context = super().get_context_data(**kwargs)
        context['filter'] = MailingFilter(self.request.GET, queryset=self.get_queryset())
        return context
