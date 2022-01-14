from django.db import models

from .validators import validate_number_or_range_str


class Genus(models.Model):
    class Meta:
        verbose_name = "Род"
        verbose_name_plural = "Род"
    name = models.CharField(max_length=50, verbose_name='Название рода')
    photo = models.ImageField(upload_to='images/', verbose_name='Фото цветка')

    def __str__(self):
        return self.name


class Species(models.Model):
    class Meta:
        verbose_name = "Вид"
        verbose_name_plural = "Вид"
    name = models.CharField(max_length=50, verbose_name='Название вида')
    genus = models.ForeignKey('Genus', on_delete=models.CASCADE, verbose_name="Род")

    def __str__(self):
        return f'{self.genus} {self.name}'


class SupplySize(models.Model):
    class Meta:
        verbose_name = "Размер поставки"
        verbose_name_plural = "Размер поставки"
    size = models.CharField(max_length=50, verbose_name='Размер поставки')

    def clean(self):
        validate_number_or_range_str(self.size, 'Размер поставки')

    def __str__(self):
        return self.size


class Warehouse(models.Model):
    class Meta:
        verbose_name = "Склад"
        verbose_name_plural = "Склад"
    amount = models.IntegerField(verbose_name='Доступное количество')
    item = models.OneToOneField('Item', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.item}, доступное количество {self.amount}'


class Item(models.Model):
    class Meta:
        verbose_name = 'Позицию'
        verbose_name_plural = 'Позиция'
    AVAILABLE = 'AV'
    ENDED = 'EN'
    REPRODUCTION = 'RE'
    AVAILABILITY_CHOICES = [
        (AVAILABLE, 'доступно'),
        (ENDED, 'закончились'),
        (REPRODUCTION, 'на размножении'),
    ]
    availability = models.CharField(
        max_length=2,
        choices=AVAILABILITY_CHOICES,
        default=AVAILABLE,
        verbose_name='Доступность'
    )
    flower = models.ForeignKey('Flower', on_delete=models.CASCADE, verbose_name='Цветок', related_name="items")
    supply_size = models.ForeignKey('SupplySize', on_delete=models.CASCADE, verbose_name='Размер поставки')
    price = models.IntegerField(default=0, verbose_name='Цена')

    def __str__(self):
        if self.availability == self.AVAILABLE:
            return f'{self.flower.variety}, размер поставки: {self.supply_size}, по цене: {self.price}'
        else:
            return f'{self.flower.variety} {self.get_availability_display()}'


class Flower(models.Model):
    class Meta:
        verbose_name = 'Цветок'
        verbose_name_plural = 'Цветок'
    variety = models.CharField(max_length=200, verbose_name='Сорт')
    manufacturer = models.CharField(max_length=100, blank=True, verbose_name='Производитель')
    species = models.ForeignKey('Species', on_delete=models.CASCADE, verbose_name='Вид')
    height = models.IntegerField(default=0, verbose_name='Высота')
    SIZE_CHOICES = [
        ('Маленький, 10-15', '10-15'),
        ('Средний, 15-20', '15-20'),
        ('Большой, 20-25', '20-25'),
    ]
    size = models.CharField(
        max_length=20,
        choices=SIZE_CHOICES,
        default='small',
        verbose_name='Размер цветка'
    )
    florescence = models.CharField(max_length=200, default='', verbose_name='Цветение')
    delivery = models.CharField(max_length=200, default='', blank=True, verbose_name='Доставка')
    main_photo = models.ImageField(upload_to='images/', verbose_name='Основное фото цветка')
    description = models.TextField(max_length=2000, default='', blank=True, verbose_name='Описание')

    def __str__(self):
        return f'{self.variety} {self.species}'


class OrderItem(models.Model):
    class Meta:
        verbose_name = 'Позицию заказа'
        verbose_name_plural = 'Позиция заказа'
    order = models.ForeignKey('Order', on_delete=models.CASCADE, verbose_name='Заказ')
    item = models.ForeignKey('Item', on_delete=models.CASCADE)
    amount = models.IntegerField(default=0, verbose_name='Количество')

    def __str__(self):
        return f'Заказ номер:{self.order.pk}, позиция:{self.item}, количество: {self.amount}'


class Order(models.Model):
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказ'
    user = models.ForeignKey('Customer', on_delete=models.CASCADE, verbose_name='Покупатель')
    order_price = models.IntegerField(default=0, verbose_name='Сумма заказа')
    prepayment = models.IntegerField(default=0, verbose_name='Предоплата')

    def __str__(self):
        return f'Заказ номер:{self.pk}, сумма заказа:{self.order_price}, предоплачено: {self.prepayment} '


class Customer(models.Model):
    class Meta:
        verbose_name = 'Покупателя'
        verbose_name_plural = 'Покупатель'
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    address = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name


class Image(models.Model):
    class Meta:
        verbose_name = 'Картинку'
        verbose_name_plural = 'Картинка'
    flower = models.ForeignKey('Flower', on_delete=models.CASCADE, verbose_name='Цветок', related_name="images")
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return str(self.flower)
