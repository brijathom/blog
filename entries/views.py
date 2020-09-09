from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Entry
from .forms import EntryForm


class HomeView(ListView):
    model = Entry
    template_name = 'entries/index.html'
    context_object_name = 'blog_entries'
    ordering = ['-entry_date']
    paginate_by = 3


class EntryView(DetailView):
    model = Entry
    template_name = 'entries/entry_detail.html'


class CreateEntryView(CreateView):
    model = Entry
    form_class = EntryForm
    template_name = 'entries/create_entry.html'

    def form_valid(self, form):
        form.instance.entry_author = self.request.user
        return super().form_valid(form)


class UpdateEntryView(UpdateView):
    model = Entry
    form_class = EntryForm
    template_name = 'entries/update_entry.html'


class DeleteEntryView(UpdateView):
    model = Entry
    form_class = EntryForm
    template_name = 'entries/update_entry.html'
