from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView
from django.views.generic.base import TemplateView

from .forms import FeedBackForm, BetForm
from .models import Lot, Event, Bet


class ContextMixin:
    context = {
        'site_title': 'Auction',
        'facebook': 'https://facebook.com',
        'twitter': 'https://twitter.com',
        'github': 'https://github.com',
    }


class IndexView(ContextMixin, TemplateView):
    template_name = 'online_auction/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data()
        context.update(self.context)
        context['feedback_form'] = FeedBackForm()
        context['user'] = self.request.user
        context['lots'] = Lot.objects.all()
        return context

    @staticmethod
    def post(request: HttpRequest):
        form = FeedBackForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'online_auction/index.html', {
            'feedback_form': form,
        })


class SearchView(View):
    template_name = 'online_auction/search_page.html'

    def get(self, request):
        lots = Lot.objects.all()
        return render(request, self.template_name, {'lots': lots, 'is_user_lots': False})


class AboutView(ContextMixin, TemplateView):
    template_name = 'online_auction/about.html'

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data()
        context.update(self.context)
        context['feedback_form'] = FeedBackForm()
        return context

    @staticmethod
    def post(request: HttpRequest):
        form = FeedBackForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'online_auction/about.html', {
            'feedback_form': form,
        })


class LotCreateView(CreateView):
    template_name = 'online_auction/lot_add.html'
    model = Lot
    fields = ('name', 'category', 'image', 'description')
    success_url = '/accounts/profile'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class LotUpdateView(UpdateView):
    template_name = 'online_auction/lot_update.html'
    model = Lot
    fields = ('name', 'category', 'image', 'description')
    success_url = '/accounts/profile'


class LotDetailView(DetailView):
    template_name = 'online_auction/lot_detail.html'
    model = Lot
    fields = ('name', 'category', 'image', 'description')


class LotDeleteView(DeleteView):
    template_name = 'online_auction/lot_delete.html'
    model = Lot
    success_url = "/accounts/profile"


class ProfileView(LoginRequiredMixin, View):
    template_name = 'online_auction/search_page.html'

    def get(self, request):
        lots = Lot.objects.filter(owner=request.user)
        return render(request, self.template_name, {'lots': lots, 'is_user_lots': True})


class AuctionSearchView(View):
    template_name = 'online_auction/auction_search_page.html'

    def get(self, request):
        events = Event.objects.all()
        return render(request, self.template_name, {'events': events})


class AuctionCreateView(CreateView):
    template_name = 'online_auction/auction_add.html'
    model = Event
    fields = (
        'name', 'lot', 'buyout_price', 'start_price', 'start_date',
        'end_date'
    )
    success_url = '/auction-search'

    def form_valid(self, form):
        form.instance.is_started = True
        return super().form_valid(form)


class AuctionDetailView(LoginRequiredMixin, View):
    template_name = 'online_auction/auction_detail.html'
    model = Event
    fields = ('name', 'lot', 'buyout_price', 'start_price', 'start_date', 'end_date')

    def get(self, request, pk):
        event = Event.objects.filter(id=pk)[0]
        bets = Bet.objects.filter(event=event)
        return render(request, self.template_name, {'bets': bets, 'event': event})

    @staticmethod
    def post(request, pk):
        form = BetForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect(f"/auction/{form.instance.event.id}/detail/")
