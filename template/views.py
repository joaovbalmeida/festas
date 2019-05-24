from django.views.generic.base import TemplateView
from .models import Event
# Create your views here.

class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['events'] = Event.objects.all()
        return context

class EventsView(TemplateView):
    template_name = "event.html"

    def get_context_data(self, **kwargs):
        context = super(EventsView, self).get_context_data(**kwargs)
        context['event'] = Event.objects.get(pk=kwargs['event_id'])
        return context