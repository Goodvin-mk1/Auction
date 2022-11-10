from django.contrib.auth.models import User
from django.http import HttpRequest
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from rest_framework.viewsets import ModelViewSet
from .models import Lot
from .serializers import LotSerializer
from .forms import FeedBackForm


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

    def post(self, request: HttpRequest):
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
        return render(request, self.template_name, {'lots': lots})
