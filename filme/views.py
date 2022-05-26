from django.shortcuts import render
from .models import Filme
from django.views.generic import TemplateView, ListView, DetailView


class Homepage(TemplateView):
    template_name = 'homepage.html'


class HomeFilmes(ListView):
    template_name = 'homefilmes.html'
    model = Filme
    # object_list


class Detalhesfilme(DetailView):
    template_name = 'detalhesfilme.html'
    model = Filme
    # object

    def get(self, request, *args, **kwargs):
        # descobrir qual filme esta acessando
        filme = self.get_object()
        # somar 1 nas visualizações daquele filme
        filme.visualizacoes += 1
        filme.save()
        usuario = request.user
        usuario.filmes_vistos.add(filme)
        return super().get(request, *args, **kwargs) # redireciona o usuario para a url final

    def get_context_data(self, **kwargs):
        context = super(Detalhesfilme, self).get_context_data(**kwargs)
        # Filtrar a tabela de filmes pegando os da mesma categoria
        filmes_relacionados = Filme.objects.filter(categoria=self.get_object().categoria)[0:5]
        context['filmes_relacionados'] = filmes_relacionados
        return context


class PesquisaFilme(ListView):
    template_name = 'pesquisa.html'
    model = Filme

    def get_queryset(self):
        termo_pesquisa = self.request.GET.get('query')
        if termo_pesquisa:
            object_list = self.model.objects.filter(titulo__icontains=termo_pesquisa)
            return object_list
        else:
            return None