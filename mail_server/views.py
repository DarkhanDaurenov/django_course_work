from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.core.cache import cache
from blog.models import BlogPost
from mail_server.models import Client, Distribution, Letter, TryLetter
from django.shortcuts import render

class ManagerRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.groups.filter(name='Managers').exists()


class ClientListView(ManagerRequiredMixin, ListView):
    model = Client
    template_name = 'mail_server/client_list.html'
    context_object_name = 'clients'


class ClientDetailView(ManagerRequiredMixin, DetailView):
    model = Client
    template_name = 'mail_server/client_detail.html'
    context_object_name = 'client'


class ClientCreateView(ManagerRequiredMixin, CreateView):
    model = Client
    template_name = 'mail_server/client_form.html'
    fields = ['email', 'name', 'surname', 'second_name', 'comments']
    success_url = reverse_lazy('mail_server:client_list')


class ClientUpdateView(ManagerRequiredMixin,UpdateView):
    model = Client
    template_name = 'mail_server/client_form.html'
    fields = ['email', 'name', 'surname', 'second_name', 'comments']
    success_url = reverse_lazy('mail_server:client_list')


class ClientDeleteView(ManagerRequiredMixin, DeleteView):
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


class HomeView(TemplateView):
    template_name = 'mail_server/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        cache_key = 'home_page_data'
        context_data = cache.get(cache_key)

        if not context_data:
            total_distributions = Distribution.objects.count()
            active_distributions = Distribution.objects.filter(status='active').count()
            unique_clients = Client.objects.count()
            random_posts = BlogPost.objects.order_by('?')[:5]

            context_data = {
                'total_distributions': total_distributions,
                'active_distributions': active_distributions,
                'unique_clients': unique_clients,
                'random_posts': random_posts
            }

            cache.set(cache_key, context_data, timeout=600)

        context.update(context_data)
        return context