from django.urls import path
from .views import (
    ClientListView, ClientDetailView, ClientCreateView, ClientUpdateView, ClientDeleteView,
    DistributionListView, DistributionDetailView, DistributionCreateView, DistributionUpdateView,
    DistributionDeleteView, LetterListView, LetterDetailView, TryLetterListView, TryLetterDetailView, LetterCreateView,
    LetterDeleteView, LetterUpdateView
)

app_name = 'mail_server'

urlpatterns = [
    path('', ClientListView.as_view(), name='client_list'),
    path('clients/<int:pk>/', ClientDetailView.as_view(), name='client_detail'),
    path('clients/create/', ClientCreateView.as_view(), name='client_create'),
    path('clients/<int:pk>/edit/', ClientUpdateView.as_view(), name='client_update'),
    path('clients/<int:pk>/delete/', ClientDeleteView.as_view(), name='client_delete'),
    path('distributions/', DistributionListView.as_view(), name='distribution_list'),
    path('distributions/<int:pk>/', DistributionDetailView.as_view(), name='distribution_detail'),
    path('distributions/create/', DistributionCreateView.as_view(), name='distribution_create'),
    path('distributions/<int:pk>/edit/', DistributionUpdateView.as_view(), name='distribution_update'),
    path('distributions/<int:pk>/delete/', DistributionDeleteView.as_view(), name='distribution_delete'),
    path('letters/', LetterListView.as_view(), name='letter_list'),
    path('letters/<int:pk>/', LetterDetailView.as_view(), name='letter_detail'),
    path('letters/create/', LetterCreateView.as_view(), name='letter_create'),
    path('letters/<int:pk>/edit/', LetterUpdateView.as_view(), name='letter_update'),
    path('letters/<int:pk>/delete/', LetterDeleteView.as_view(), name='letter_delete'),
    path('try-letters/', TryLetterListView.as_view(), name='try_letter_list'),
    path('try-letters/<int:pk>/', TryLetterDetailView.as_view(), name='try_letter_detail'),
    path('letters/create/', LetterCreateView.as_view(), name='letter_create')

]