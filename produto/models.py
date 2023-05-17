from django.db import models

# Create your models here.
"""             
        Variacao:
            nome - char
            produto - FK Produto
            preco - Float
            preco_promocional - Float
            estoque - Int
"""


class Produto(models.Model):
    nome = models.CharField(max_length=255)
    descricao_curta = models.TextField(max_length=300)
    descricao_Longa = models.TextField()
    imagem = models.ImageField(
        upload_to='produto_imagens/%y/%m/', blank=True, null=True)
    slug = models.SlugField(unique=True)
    preco_marketing = models.FloatField(default=0)
    preco_marketing_promocional = models.FloatField(default=0)
    tipo = models.CharField(
        default="v",
        max_length=1,
        choices=(
            ('V', 'Variação'),
            ('S', 'Simples'),
        )
    )

    @staticmethod
    def resize_image(img, new_width=800):
        print(img.name)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        max_image_size = 800
        if self.imagem:
            self.resize_image(self.imagem, max_image_size)

    def __str__(self):
        return self.nome
