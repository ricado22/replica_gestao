from django.db.models import Sum
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
from startup.models import Funcionario, Produto, Venda
from startup.forms import CadastraFuncionarioForm, CadastraProdutoForm, CadastraVendaForm


# PÁGINA PRINCIPAL
# ----------------------------------------------

class HomeView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data()

        context['vendas'] = Venda.objetos.all()

        # Soma de vendas por funcionário
        context['vendas_funcionario'] = \
            Venda.objetos.values('funcionario__nome').annotate(
                numero_vendas=Sum('produto'),
                total_vendas=Sum('produto__preco'),
                media_venda=Sum('produto__preco')/Sum('produto')
        )

        # Total em vendas
        context['total_vendas'] = Venda.objetos.aggregate(
            vendas=Sum('produto__preco'))

        # Quantidade total de vendas
        context['qtde_vendas'] = Venda.objetos.count()

        return context


# PÁGINA PRINCIPAL FUNCIONÁRIOS
# ----------------------------------------------

class HomeFuncionarioView(TemplateView):
    template_name = "comercial/funcionarios/index.html"


# LISTA DE FUNCIONÁRIOS
# ----------------------------------------------

class ListaFuncionariosView(ListView):
    template_name = "comercial/funcionarios/lista.html"
    model = Funcionario
    context_object_name = "funcionarios"


# CADASTRAMENTO DE FUNCIONÁRIOS
# ----------------------------------------------

class CriaFuncionarioView(CreateView):
    template_name = "comercial/funcionarios/cria.html"
    model = Funcionario
    form_class = CadastraFuncionarioForm
    success_url = reverse_lazy("startup:lista_funcionarios")


# ATUALIZAÇÃO DE FUNCIONÁRIOS
# ----------------------------------------------

class AtualizaFuncionarioView(UpdateView):
    template_name = "comercial/funcionarios/atualiza.html"
    model = Funcionario
    fields = '__all__'
    context_object_name = 'funcionario'
    success_url = reverse_lazy("startup:lista_funcionarios")


# EXCLUSÃO DE FUNCIONÁRIOS
# ----------------------------------------------

class DeletaFuncionarioView(DeleteView):
    template_name = "comercial/funcionarios/exclui.html"
    model = Funcionario
    context_object_name = 'funcionario'
    success_url = reverse_lazy("startup:lista_funcionarios")


# PÁGINA PRINCIPAL PRODUTOS
# ----------------------------------------------

class HomeProdutoView(TemplateView):
    template_name = "comercial/produtos/index.html"


# LISTA DE PRODUTOS
# ----------------------------------------------

class ListaProdutosView(ListView):
    template_name = "comercial/produtos/lista.html"
    model = Produto
    context_object_name = "produtos"


# CADASTRAMENTO DE PRODUTOS
# ----------------------------------------------

class CriaProdutoView(CreateView):
    template_name = "comercial/produtos/cria.html"
    model = Produto
    form_class = CadastraProdutoForm
    success_url = reverse_lazy("startup:lista_produtos")


# ATUALIZAÇÃO DE PRODUTOS
# ----------------------------------------------

class AtualizaProdutoView(UpdateView):
    template_name = "comercial/produtos/atualiza.html"
    model = Produto
    fields = '__all__'
    context_object_name = 'produto'
    success_url = reverse_lazy("startup:lista_produtos")


# EXCLUSÃO DE PRODUTOS
# ----------------------------------------------

class DeletaProdutoView(DeleteView):
    template_name = "comercial/produtos/exclui.html"
    model = Produto
    context_object_name = 'produto'
    success_url = reverse_lazy("startup:lista_produtos")


# PÁGINA PRINCIPAL VENDAS
# ----------------------------------------------

class HomeVendaView(TemplateView):
    template_name = "comercial/vendas/index.html"


# LISTA DE VENDAS
# ----------------------------------------------

class ListaVendasView(ListView):
    template_name = "comercial/vendas/lista.html"
    model = Venda
    context_object_name = "vendas"


# CADASTRAMENTO DE VENDAS
# ----------------------------------------------

class CriaVendaView(CreateView):
    template_name = "comercial/vendas/cria.html"
    model = Venda
    form_class = CadastraVendaForm
    success_url = reverse_lazy("startup:cadastra_venda")


# ATUALIZAÇÃO DE VENDAS
# ----------------------------------------------

class AtualizaVendaView(UpdateView):
    template_name = "comercial/vendas/atualiza.html"
    model = Venda
    fields = '__all__'
    context_object_name = 'venda'
    success_url = reverse_lazy("startup:lista_vendas")


# EXCLUSÃO DE VENDAS
# ----------------------------------------------

class DeletaVendaView(DeleteView):
    template_name = "comercial/vendas/exclui.html"
    model = Venda
    context_object_name = 'venda'
    success_url = reverse_lazy("startup:lista_vendas")
