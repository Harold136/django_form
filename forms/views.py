from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse
from django.template import loader
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .forms import CreateForm
from .models import Post, languages

def index(request):
    mymembers = Post.objects.all().values()
    template = loader.get_template('forms/base.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context,request))


class List(ListView):
    model = Post
    context_object_name = "Create"
    template_name = "forms/create.html"
    
class Create(CreateView):
    model = Post
    template_name = 'forms/create.html'
    form_class = CreateForm

    def get_success_url(self):
        return reverse('results', kwargs={'pk': self.object.pk})


class Results(DetailView):
    model = Post
    context_object_name = 'student'
    template_name = 'forms/create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        selected = set(self.object.languages.split(','))
        context['programming_languages'] = [
            label for value, label in languages if value in selected
        ]
        return context

