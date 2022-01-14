from django.contrib import admin
from .models import Genus, Species, SupplySize, Warehouse, Item, Flower, Order, OrderItem, Customer, Image

admin.site.register(Genus)
admin.site.register(Species)
admin.site.register(SupplySize)
admin.site.register(Warehouse)
admin.site.register(Item)
admin.site.register(Flower)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Customer)
admin.site.register(Image)
