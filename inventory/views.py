# from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib import messages
# from .models import Item, Transaction
# from django.db.models import F  # ✅ for comparing fields in queries


# # def dashboard(request):
# #     total_items = Item.objects.count()
# #     low_stock = Item.objects.filter(quantity__lte=F('reorder_level')).count()
# #     out_stock = Item.objects.filter(quantity=0).count()
# #     items = Item.objects.all()
# #     context = {
# #         'total_items': total_items,
# #         'low_stock': low_stock,
# #         'out_stock': out_stock,
# #         'items': items
# #     }
# #     return render(request, 'inventory/dashboard.html', context)

# PREDEFINED_CATEGORIES = ["Sensor","Connector","Resistor","Microcontroller"]

# def dashboard(request):
#     total_items = Item.objects.count()
#     low_stock = Item.objects.filter(quantity__lte=F('reorder_level')).count()
#     out_stock = Item.objects.filter(quantity=0).count()
#     items = Item.objects.all()
#     context = {
#         'total_items': total_items,
#         'low_stock': low_stock,
#         'out_stock': out_stock,
#         'items': items,
#         'PREDEFINED_CATEGORIES': PREDEFINED_CATEGORIES
#     }
#     return render(request, 'inventory/dashboard.html', context)

# def inventory_list(request):
#     items = Item.objects.all()
#     return render(request, 'inventory/inventory_list.html', {'items': items})


# # def add_item(request):
# #     if request.method == "POST":
# #         name = request.POST.get('name')
# #         category = request.POST.get('category')
# #         quantity = request.POST.get('quantity')
# #         reorder_level = request.POST.get('reorder_level')
# #         unit_price = request.POST.get('unit_price')
# #         supplier = request.POST.get('supplier')
# #         location = request.POST.get('location')
# #         description = request.POST.get('description')

# #         Item.objects.create(
# #             name=name, category=category, quantity=quantity,
# #             reorder_level=reorder_level, unit_price=unit_price,
# #             supplier=supplier, location=location, description=description
# #         )
# #         messages.success(request, "Item added successfully!")
# #         return redirect('inventory_list')

# #     return render(request, 'inventory/add_item.html')

# # def add_item(request):
# #     if request.method == "POST":
# #         name = request.POST.get('name')
# #         category = request.POST.get('category')
# #         custom_category = request.POST.get('custom_category')
# #         quantity = request.POST.get('quantity')
# #         reorder_level = request.POST.get('reorder_level')
# #         unit_price = request.POST.get('unit_price')
# #         supplier = request.POST.get('supplier')
# #         location = request.POST.get('location')
# #         description = request.POST.get('description')

# #         Item.objects.create(
# #             name=name,
# #             category=category,
# #             custom_category=custom_category,
# #             quantity=quantity,
# #             reorder_level=reorder_level,
# #             unit_price=unit_price,
# #             supplier=supplier,
# #             location=location,
# #             description=description
# #         )
# #         messages.success(request, "Item added successfully!")
# #         return redirect('inventory_list')
# #     return render(request, 'inventory/add_item.html')

# def add_item(request):
#     if request.method == "POST":
#         name = request.POST.get('name')
#         category = request.POST.get('category')
#         custom_category = request.POST.get('custom_category')
#         quantity = request.POST.get('quantity')
#         reorder_level = request.POST.get('reorder_level')
#         unit_price = request.POST.get('unit_price')
#         supplier = request.POST.get('supplier')
#         location = request.POST.get('location')
#         description = request.POST.get('description')

#         # Use custom category if "Other" is selected
#         if category == 'Other' and custom_category:
#             final_category = custom_category
#         else:
#             final_category = category

#         Item.objects.create(
#             name=name,
#             category=final_category,
#             quantity=quantity,
#             reorder_level=reorder_level,
#             unit_price=unit_price,
#             supplier=supplier,
#             location=location,
#             description=description
#         )
#         messages.success(request, "Item added successfully!")
#         return redirect('inventory_list')

#     return render(request, 'inventory/add_item.html')


# # def edit_item(request, item_id):
# #     item = get_object_or_404(Item, id=item_id)
# #     if request.method == "POST":
# #         item.name = request.POST.get('name')
# #         item.category = request.POST.get('category')
# #         item.quantity = request.POST.get('quantity')
# #         item.reorder_level = request.POST.get('reorder_level')
# #         item.unit_price = request.POST.get('unit_price')
# #         item.supplier = request.POST.get('supplier')
# #         item.location = request.POST.get('location')
# #         item.description = request.POST.get('description')
# #         item.save()
# #         messages.success(request, "Item updated successfully!")
# #         return redirect('inventory_list')

# #     return render(request, 'inventory/edit_item.html', {'item': item})

# # def edit_item(request, item_id):
# #     item = get_object_or_404(Item, id=item_id)
# #     if request.method == "POST":
# #         name = request.POST.get('name')
# #         category = request.POST.get('category')
# #         custom_category = request.POST.get('custom_category')
# #         quantity = request.POST.get('quantity')
# #         reorder_level = request.POST.get('reorder_level')
# #         unit_price = request.POST.get('unit_price')
# #         supplier = request.POST.get('supplier')
# #         location = request.POST.get('location')
# #         description = request.POST.get('description')

# #         # Update item fields
# #         item.name = name
# #         # If user selected 'Other' and entered custom category, use it
# #         if category == 'Other' and custom_category:
# #             item.category = custom_category
# #         else:
# #             item.category = category

# #         item.quantity = quantity
# #         item.reorder_level = reorder_level
# #         item.unit_price = unit_price
# #         item.supplier = supplier
# #         item.location = location
# #         item.description = description

# #         item.save()
# #         messages.success(request, "Item updated successfully!")
# #         return redirect('inventory_list')

# #     return render(request, 'inventory/edit_item.html', {'item': item})

# def edit_item(request, item_id):
#     item = get_object_or_404(Item, id=item_id)
#     if request.method == "POST":
#         name = request.POST.get('name')
#         category = request.POST.get('category')
#         custom_category = request.POST.get('custom_category')
#         quantity = request.POST.get('quantity')
#         reorder_level = request.POST.get('reorder_level')
#         unit_price = request.POST.get('unit_price')
#         supplier = request.POST.get('supplier')
#         location = request.POST.get('location')
#         description = request.POST.get('description')

#         # Update item fields
#         item.name = name
#         if category == 'Other' and custom_category:
#             item.category = custom_category
#         else:
#             item.category = category

#         item.quantity = quantity
#         item.reorder_level = reorder_level
#         item.unit_price = unit_price
#         item.supplier = supplier
#         item.location = location
#         item.description = description

#         item.save()
#         messages.success(request, "Item updated successfully!")
#         return redirect('inventory_list')

#     return render(request, 'inventory/edit_item.html', {'item': item})


# def delete_item(request, item_id):
#     item = get_object_or_404(Item, id=item_id)
#     item.delete()
#     messages.success(request, "Item deleted successfully!")
#     return redirect('inventory_list')


# def add_stock(request, item_id):
#     item = get_object_or_404(Item, id=item_id)
#     if request.method == "POST":
#         qty = int(request.POST.get("quantity"))
#         item.quantity += qty
#         item.save()
#         Transaction.objects.create(item=item, transaction_type='IN', quantity=qty)
#         messages.success(request, f"{qty} units added to {item.name}")
#         return redirect('inventory_list')

#     return render(request, 'inventory/add_stock.html', {'item': item})


# def remove_stock(request, item_id):
#     item = get_object_or_404(Item, id=item_id)
#     if request.method == "POST":
#         qty = int(request.POST.get("quantity"))
#         if qty > item.quantity:
#             messages.error(request, "Not enough stock available")
#         else:
#             item.quantity -= qty
#             item.save()
#             Transaction.objects.create(item=item, transaction_type='OUT', quantity=qty)
#             messages.success(request, f"{qty} units removed from {item.name}")
#         return redirect('inventory_list')

#     return render(request, 'inventory/remove_stock.html', {'item': item})


# def transaction_history(request):
#     transactions = Transaction.objects.all().order_by('-date')
#     return render(request, 'inventory/transaction_history.html', {'transactions': transactions})

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Item, Transaction
from django.db.models import F

# Predefined categories for dropdown
PREDEFINED_CATEGORIES = ["Sensor", "Connector", "Resistor", "Microcontroller"]

def dashboard(request):
    total_items = Item.objects.count()
    low_stock = Item.objects.filter(quantity__lte=F('reorder_level')).count()
    out_stock = Item.objects.filter(quantity=0).count()
    items = Item.objects.all()
    context = {
        'total_items': total_items,
        'low_stock': low_stock,
        'out_stock': out_stock,
        'items': items,
        'PREDEFINED_CATEGORIES': PREDEFINED_CATEGORIES
    }
    return render(request, 'inventory/dashboard.html', context)


def inventory_list(request):
    items = Item.objects.all()
    context = {
        'items': items,
        'PREDEFINED_CATEGORIES': PREDEFINED_CATEGORIES
    }
    return render(request, 'inventory/inventory_list.html', context)


def add_item(request):
    if request.method == "POST":
        name = request.POST.get('name')
        category = request.POST.get('category')
        custom_category = request.POST.get('custom_category')
        quantity = request.POST.get('quantity')
        reorder_level = request.POST.get('reorder_level')
        unit_price = request.POST.get('unit_price')
        supplier = request.POST.get('supplier')
        location = request.POST.get('location')
        description = request.POST.get('description')

        # Use custom category if "Other" is selected
        final_category = custom_category if category == "Other" and custom_category else category

        Item.objects.create(
            name=name,
            category=final_category,
            quantity=quantity,
            reorder_level=reorder_level,
            unit_price=unit_price,
            supplier=supplier,
            location=location,
            description=description
        )
        messages.success(request, "Item added successfully!")
        return redirect('inventory_list')

    return render(request, 'inventory/add_item.html', {'PREDEFINED_CATEGORIES': PREDEFINED_CATEGORIES})


def edit_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == "POST":
        name = request.POST.get('name')
        category = request.POST.get('category')
        custom_category = request.POST.get('custom_category')
        quantity = request.POST.get('quantity')
        reorder_level = request.POST.get('reorder_level')
        unit_price = request.POST.get('unit_price')
        supplier = request.POST.get('supplier')
        location = request.POST.get('location')
        description = request.POST.get('description')

        # Update item fields
        item.name = name
        item.category = custom_category if category == "Other" and custom_category else category
        item.quantity = quantity
        item.reorder_level = reorder_level
        item.unit_price = unit_price
        item.supplier = supplier
        item.location = location
        item.description = description
        item.save()

        messages.success(request, "Item updated successfully!")
        return redirect('inventory_list')

    return render(request, 'inventory/edit_item.html', {'item': item, 'PREDEFINED_CATEGORIES': PREDEFINED_CATEGORIES})


def delete_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.delete()
    messages.success(request, "Item deleted successfully!")
    return redirect('inventory_list')


def add_stock(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == "POST":
        qty = int(request.POST.get("quantity"))
        item.quantity += qty
        item.save()
        Transaction.objects.create(item=item, transaction_type='IN', quantity=qty)
        messages.success(request, f"{qty} units added to {item.name}")
        return redirect('inventory_list')
    return render(request, 'inventory/add_stock.html', {'item': item})


def remove_stock(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == "POST":
        qty = int(request.POST.get("quantity"))
        if qty > item.quantity:
            messages.error(request, "Not enough stock available")
        else:
            item.quantity -= qty
            item.save()
            Transaction.objects.create(item=item, transaction_type='OUT', quantity=qty)
            messages.success(request, f"{qty} units removed from {item.name}")
        return redirect('inventory_list')
    return render(request, 'inventory/remove_stock.html', {'item': item})


def transaction_history(request):
    transactions = Transaction.objects.all().order_by('-date')
    context = {
        'transactions': transactions,
        'PREDEFINED_CATEGORIES': PREDEFINED_CATEGORIES
    }
    return render(request, 'inventory/transaction_history.html', context)
