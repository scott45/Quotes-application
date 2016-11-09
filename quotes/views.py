from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Quote
from django.core.urlresolvers import reverse_lazy

class IndexView(generic.ListView):
    template_name = "index.html"
    context_object_name = "quotes"

    def get_queryset(self):
        return Quote.objects.all()


class DetailView(generic.DetailView):
    model = Quote
    template_name = "detail.html"


class DepartmentCreate(CreateView):
    model = Quote
    fields = ['Name', 'Leader', 'Department_logo', 'is_favorite']
    template_name = 'department_form.html'


class DepartmentUpdate(CreateView):
    model = Quote
    fields = ['Name', 'Leader', 'Department_logo', 'is_favorite']


class DepartmentDelete(DeleteView):
    model = Quote
    success_url = reverse_lazy('index')


