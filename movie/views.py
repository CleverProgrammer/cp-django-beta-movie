from django.shortcuts import render
from django.urls import reverse_lazy
from django.db.models import Q

from django.views.generic import ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView

from .models import Movie
from .forms import MovieForm

# Create your views here.
class MovieList(ListView):
    model = Movie
    template_name = 'movies/movie_list.html'
    context_object_name = 'movies_list'

    def get_queryset(self):
    	queryset = super(MovieList,self).get_queryset()

    	if self.request.GET.get('query'):
    		q = self.request.GET.get('query')
    		queryset = queryset.filter(Q(Q(name__icontains=q)|Q(notes__icontains=q)))
    	return queryset



    def get_context_data(self, **kwargs):
        context = super(MovieList,self).get_context_data(**kwargs)
        context['myform'] = MovieForm

        return context


class MovieUpdateView(UpdateView):
    model = Movie
    form_class = MovieForm
    template_name = 'movies/edit-model.html'

    def get_success_url(self):
        return reverse_lazy('list')

class MovieDelete(DeleteView):
	model = Movie
	success_url = reverse_lazy('list')

	def delete(self, request, *args, **kwargs):
		return super(DeleteView, self).delete(request, *args, **kwargs)

class MovieCreateView(CreateView):
	model = Movie
	template_name = 'movies/create.html'
	fields = '__all__'

	def get_success_url(self):
		return reverse_lazy('list')
