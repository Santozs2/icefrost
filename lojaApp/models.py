from django.db import models

class categoria(models.Model):
    nome = models.CharField(max_length = 50, unique = True)
    def __str__(self):
        return self.nome

class fornecedor(models.Model):
    nome_empresa = models.CharField(max_length = 100)
    telefone = models.CharField(max_length = 15, unique = True)
    email = models.EmailField(max_length = 64, unique = True)

    def __str__(self):
        return self.nome_empresa

class opcaoDietica(models.Model):

    nome = models.CharField(max_length = 50, unique = True)

    def __str__(self):
        return self.nome

class sorvete(models.Model):
    sabor = models.CharField(max_length = 50)
    descricao = models.TextField(blank = True)
    preco = models.DecimalField(max_digits = 8, decimal_places = 2)
    categoria = models.ForeignKey('categoria', on_delete = models.CASCADE)
    fornecedor = models.ForeignKey('fornecedor', on_delete = models.CASCADE)
    opcoes_dieticas = models.ManyToManyField(opcaoDietica)

    def __str__(self):
        return self.sabor

class comentario(models.Model):
    autor = models.CharField(max_length = 100, blank = True, null = True)
    email = models.EmailField(max_length = 64, unique = True)
    mensagem = models.TextField()

    def __str__(self):
        return f'Comentário de {self.autor or "Anônimo"}'

    