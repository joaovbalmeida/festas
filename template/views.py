from django.views.generic.base import TemplateView
# Create your views here.

class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        return context

class EventsView(TemplateView):
    template_name = "event.html"
        
    def get_context_data(self, **kwargs):
        context = super(EventsView, self).get_context_data(**kwargs)
        return context