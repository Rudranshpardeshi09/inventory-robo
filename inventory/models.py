
# from django.db import models

# class Item(models.Model):
#     CATEGORY_CHOICES = [
#         ('Sensor', 'Sensor'),
#         ('Connector', 'Connector'),
#         ('Resistor', 'Resistor'),
#         ('Microcontroller', 'Microcontroller'),
#         ('Other', 'Other'),
#     ]

#     serial_no = models.PositiveIntegerField(unique=True, blank=True, null=True)
#     name = models.CharField(max_length=100)
#     category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
#     quantity = models.PositiveIntegerField(default=0)
#     reorder_level = models.PositiveIntegerField(default=5)
#     unit_price = models.DecimalField(max_digits=10, decimal_places=2)
#     supplier = models.CharField(max_length=100, blank=True, null=True)
#     location = models.CharField(max_length=100, blank=True, null=True)
#     description = models.TextField(blank=True, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def save(self, *args, **kwargs):
#         # Automatically assign serial number
#         if not self.serial_no:
#             last_item = Item.objects.order_by('-serial_no').first()
#             self.serial_no = (last_item.serial_no + 1) if last_item else 1
#         super().save(*args, **kwargs)

#     def stock_status(self):
#         if self.quantity == 0:
#             return "Out of Stock"
#         elif self.quantity <= self.reorder_level:
#             return "Low Stock"
#         return "In Stock"

#     def __str__(self):
#         return self.name


# class Transaction(models.Model):
#     TRANSACTION_TYPES = [
#         ('IN', 'Stock In'),
#         ('OUT', 'Stock Out'),
#     ]
#     item = models.ForeignKey(Item, on_delete=models.CASCADE)
#     transaction_type = models.CharField(max_length=3, choices=TRANSACTION_TYPES)
#     quantity = models.PositiveIntegerField()
#     date = models.DateTimeField(auto_now_add=True)
#     remarks = models.TextField(blank=True, null=True)

#     def __str__(self):
#         return f"{self.transaction_type} - {self.item.name}"

# from django.db import models

# class Item(models.Model):
#     CATEGORY_CHOICES = [
#         ('Sensor', 'Sensor'),
#         ('Connector', 'Connector'),
#         ('Resistor', 'Resistor'),
#         ('Microcontroller', 'Microcontroller'),
#         ('Other', 'Other'),
#     ]

#     serial_no = models.PositiveIntegerField(unique=True, blank=True, null=True)
#     name = models.CharField(max_length=100)
#     category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
#     quantity = models.PositiveIntegerField(default=0)
#     reorder_level = models.PositiveIntegerField(default=5)
#     unit_price = models.DecimalField(max_digits=10, decimal_places=2)
#     supplier = models.CharField(max_length=100, blank=True, null=True)
#     location = models.CharField(max_length=100, blank=True, null=True)
#     description = models.TextField(blank=True, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def save(self, *args, **kwargs):
#         # ✅ Automatically assign serial number safely
#         if not self.serial_no:
#             last_item = Item.objects.order_by('-serial_no').first()
#             self.serial_no = (last_item.serial_no + 1) if last_item and last_item.serial_no else 1
#         super().save(*args, **kwargs)

#     def stock_status(self):
#         if self.quantity == 0:
#             return "Out of Stock"
#         elif self.quantity <= self.reorder_level:
#             return "Low Stock"
#         return "In Stock"

#     def __str__(self):
#         return self.name


# class Transaction(models.Model):
#     TRANSACTION_TYPES = [
#         ('IN', 'Stock In'),
#         ('OUT', 'Stock Out'),
#     ]
#     item = models.ForeignKey(Item, on_delete=models.CASCADE)
#     transaction_type = models.CharField(max_length=3, choices=TRANSACTION_TYPES)
#     quantity = models.PositiveIntegerField()
#     date = models.DateTimeField(auto_now_add=True)
#     remarks = models.TextField(blank=True, null=True)

#     def __str__(self):
#         return f"{self.transaction_type} - {self.item.name}"

from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver


class Item(models.Model):
    CATEGORY_CHOICES = [
        ('Sensor', 'Sensor'),
        ('Connector', 'Connector'),
        ('Resistor', 'Resistor'),
        ('Microcontroller', 'Microcontroller'),
        ('Other', 'Other'),
    ]

    serial_no = models.PositiveIntegerField(unique=True, blank=True, null=True)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    custom_category = models.CharField(max_length=100, blank=True, null=True)
    quantity = models.PositiveIntegerField(default=0)
    reorder_level = models.PositiveIntegerField(default=5)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    supplier = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # def save(self, *args, **kwargs):
    #     # ✅ Automatically assign serial number safely
    #     if not self.serial_no:
    #         last_item = Item.objects.order_by('-serial_no').first()
    #         self.serial_no = (last_item.serial_no + 1) if last_item and last_item.serial_no else 1
    #     super().save(*args, **kwargs)

     # save method
    def save(self, *args, **kwargs):
        # If 'Other' is selected, use custom_category
        if self.category == 'Other' and self.custom_category:
            self.category = self.custom_category
        # Serial no logic
        if not self.serial_no:
            last_item = Item.objects.order_by('-serial_no').first()
            self.serial_no = (last_item.serial_no + 1) if last_item and last_item.serial_no else 1
        super().save(*args, **kwargs)

    def stock_status(self):
        if self.quantity == 0:
            return "Out of Stock"
        elif self.quantity <= self.reorder_level:
            return "Low Stock"
        return "In Stock"

    def __str__(self):
        return self.name


class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ('IN', 'Stock In'),
        ('OUT', 'Stock Out'),
    ]
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=3, choices=TRANSACTION_TYPES)
    quantity = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add=True)
    remarks = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.transaction_type} - {self.item.name}"


# ✅ Signal to reorder serial numbers automatically after an item is deleted
@receiver(post_delete, sender=Item)
def reorder_serial_numbers(sender, instance, **kwargs):
    """
    After an item is deleted, this will reorder serial numbers sequentially.
    """
    items = Item.objects.order_by('serial_no')
    for index, item in enumerate(items, start=1):
        if item.serial_no != index:
            item.serial_no = index
            item.save(update_fields=['serial_no'])
