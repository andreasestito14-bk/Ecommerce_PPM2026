from django.conf import settings
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nome Categoria")
    slug = models.SlugField(unique=True, verbose_name="Slug URL")
    description = models.TextField(blank=True, verbose_name="Descrizione")

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorie"

    def __str__(self):
        return self.name


class Product(models.Model):
    # Relazione 1: Uno-a-Molti con Category
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products", verbose_name="Categoria")
    name = models.CharField(max_length=200, verbose_name="Nome Prodotto")
    description = models.TextField(verbose_name="Descrizione")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Prezzo (€)")
    stock = models.PositiveIntegerField(default=0, verbose_name="Quantità Disponibile")
    image_url = models.URLField(max_length=500, blank=True, null=True, verbose_name="URL Immagine")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data Aggiunta")

    class Meta:
        verbose_name = "Prodotto"
        verbose_name_plural = "Prodotti"

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'In Attesa'),
        ('completed', 'Completato'),
        ('cancelled', 'Annullato'),
    ]

    # Relazione 2: Uno-a-Molti col CustomUser
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="orders", verbose_name="Cliente")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data Ordine")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name="Stato")
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name="Prezzo Totale")

    class Meta:
        verbose_name = "Ordine"
        verbose_name_plural = "Ordini"

    def __str__(self):
        return f"Ordine #{self.id} - {self.user.username}"

    @property
    def get_total(self):
        """Calcola il totale complessivo dell'intero carrello"""
        return sum(item.get_total_item_price for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items", verbose_name="Ordine")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Prodotto")
    quantity = models.PositiveIntegerField(default=1, verbose_name="Quantità")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Prezzo Unitario")

    def __str__(self):
        return f"{self.quantity}x {self.product.name} (Ordine #{self.order.id})"

    @property
    def get_total_item_price(self):
        return self.price * self.quantity