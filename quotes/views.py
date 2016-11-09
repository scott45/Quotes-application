from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Quote
from django.core.urlresolvers import reverse_lazy


class IndexView(generic.ListView):
    template_name = "index.html"
    context_object_name = "all_quotes"

    def get_queryset(self):
        return Quote.objects.all()


class DetailView(generic.DetailView):
    model = Quote
    template_name = "quotes/detail.html"


class QuoteCreate(CreateView):
    model = Quote
    fields = ['title', 'submitter', 'description']
    template_name = 'quotes/quotes_form.html'


class QuoteUpdate(UpdateView):
    model = Quote
    fields = ['title', 'submitter', 'description']


class QuoteDelete(DeleteView):
    model = Quote
    success_url = reverse_lazy('index')
