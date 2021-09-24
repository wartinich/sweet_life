from django.db import models


class Product(models.Model):

    CAKE = 'Cake'
    CHESS_CAKE = 'Chesscake'
    MARSHMALLOWS = 'Marshmello'
    CAP_CAKE = 'Capcake'

    CHOICE_CATEGORY = {
        (CAKE, 'Cake'),
        (CHESS_CAKE, 'Chesscake'),
        (MARSHMALLOWS, 'Marshmello'),
        (CAP_CAKE, 'Capcake'),
    }

    title = models.CharField(verbose_name='Title', max_length=100, blank=False, null=False)
    slug = models.SlugField(verbose_name='Slug', max_length=110, unique=True)
    category = models.CharField(verbose_name='Category', max_length=60, choices=CHOICE_CATEGORY, default=CAKE)
    short_info = models.CharField(verbose_name='Short info', max_length=150, blank=False)
    image = models.ImageField(verbose_name='Image', upload_to='products/', blank=False)
    price = models.DecimalField(verbose_name='Price', max_digits=8, decimal_places=0, blank=False)
    created_at = models.DateTimeField(verbose_name='Date', auto_now=True, auto_now_add=False)
    available = models.BooleanField(verbose_name='Available', default=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'product'


class Advertisement(models.Model):
    name = models.CharField(verbose_name='Name', max_length=150, blank=False)
    image = models.ImageField(verbose_name='Image', upload_to='advertisement/')
    created_at = models.DateTimeField(verbose_name='Date', auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'advertisement_product'

