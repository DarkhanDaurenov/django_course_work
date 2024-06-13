from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from mail_server.models import Client, Distribution, Letter, TryLetter


class ClientListView(ListView):
    model = Client
    template_name = 'mail_server/client_list.html'
    context_object_name = 'clients'


class ClientDetailView(DetailView):
    model = Client
    template_name = 'mail_server/client_detail.html'
    context_object_name = 'client'


class ClientCreateView(CreateView):
    model = Client
    template_name = 'mail_server/client_form.html'
    fields = ['email', 'name', 'surname', 'second_name', 'comments']
    success_url = reverse_lazy('mail_server:client_list')


class ClientUpdateView(UpdateView):
    model = Client
    template_name = 'mail_server/client_form.html'
    fields = ['email', 'name', 'surname', 'second_name', 'comments']
    success_url = reverse_lazy('mail_server:client_list')


class ClientDeleteView(DeleteView):
    model = Client
    template_name = 'mail_server/client_confirm_delete.html'
    success_url = reverse_lazy('mail_server:client_list')


class DistributionListView(ListView):
    model = Distribution
    template_name = 'mail_server/distribution_list.html'
    context_object_name = 'distributions'


class DistributionDetailView(DetailView):
    model = Distribution
    template_name = 'mail_server/distribution_detail.html'
    context_object_name = 'distribution'


class DistributionCreateView(CreateView):
    model = Distribution
    template_name = 'mail_server/distribution_form.html'
    fields = ['clients', 'message', 'period', 'status']
    success_url = reverse_lazy('mail_server:distribution_list')


class DistributionUpdateView(UpdateView):
    model = Distribution
    template_name = 'mail_server/distribution_form.html'
    fields = ['clients', 'message', 'period', 'status']
    success_url = reverse_lazy('mail_server:distribution_list')


class DistributionDeleteView(DeleteView):
    model = Distribution
    template_name = 'mail_server/distribution_confirm_delete.html'
    success_url = reverse_lazy('mail_server:distribution_list')


class LetterListView(ListView):
    model = Letter
    template_name = 'mail_server/letter_list.html'
    context_object_name = 'letters'


class LetterCreateView(CreateView):
    model = Letter
    template_name = 'mail_server/letter_form.html'
    fields = ['title_message', 'body_message']
    success_url = reverse_lazy('mail_server:letter_list')


class LetterDetailView(DetailView):
    model = Letter
    template_name = 'mail_server/letter_detail.html'
    context_object_name = 'letter'


class LetterUpdateView(UpdateView):
    model = Letter
    template_name = 'mail_server/letter_form.html'
    fields = ['title_message', 'body_message']
    success_url = reverse_lazy('mail_server:letter_list')


class LetterDeleteView(DeleteView):
    model = Letter
    template_name = 'mail_server/letter_confirm_delete.html'
    success_url = reverse_lazy('mail_server:letter_list')


class TryLetterListView(ListView):
    model = TryLetter
    template_name = 'mail_server/try_letter_list.html'
    context_object_name = 'try_letters'


class TryLetterDetailView(DetailView):
    model = TryLetter
    template_name = 'mail_server/try_letter_detail.html'
    context_object_name = 'try_letter'
