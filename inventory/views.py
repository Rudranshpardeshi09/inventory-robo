# from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib import messages
# from .models import Item, Transaction
# from django.db.models import F
# from django.core.paginator import Paginator
# from django.utils import timezone  # ✅ for updating transaction timestamp
# from django.db import transaction
# from .models import Item, Issuance
# from .forms import IssuanceForm, ReceiveForm

# # Predefined categories for dropdown
# PREDEFINED_CATEGORIES = ["Sensor", "Connector", "Resistor", "Microcontroller"]

# def dashboard(request):
#     total_items = Item.objects.count()
#     low_stock = Item.objects.filter(quantity__gt=0, quantity__lte=F('reorder_level')).count()
#     out_stock = Item.objects.filter(quantity=0).count()
#     items = Item.objects.all().order_by('serial_no')
#     paginator = Paginator(items, 10)  # 10 items per page
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     context = {
#         'total_items': total_items,
#         'low_stock': low_stock,
#         'out_stock': out_stock,
#         'items': items,
#         'PREDEFINED_CATEGORIES': PREDEFINED_CATEGORIES,
#         'page_obj': page_obj,
#     }
#     return render(request, 'inventory/dashboard.html', context)


# def inventory_list(request):
#     items = Item.objects.all().order_by('serial_no')
#     paginator = Paginator(items, 10)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     context = {
#         'items': items,
#         'PREDEFINED_CATEGORIES': PREDEFINED_CATEGORIES,
#         'page_obj': page_obj,
#     }
#     return render(request, 'inventory/inventory_list.html', context)


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

# #         # Use custom category if "Other" is selected
# #         final_category = custom_category if category == "Other" and custom_category else category

# #         Item.objects.create(
# #             name=name,
# #             category=final_category,
# #             quantity=quantity,
# #             reorder_level=reorder_level,
# #             unit_price=unit_price,
# #             supplier=supplier,
# #             location=location,
# #             description=description
# #         )
# #         messages.success(request, "Item added successfully!")
# #         return redirect('inventory_list')

# #     return render(request, 'inventory/add_item.html', {'PREDEFINED_CATEGORIES': PREDEFINED_CATEGORIES})
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

#         # Convert numeric fields safely
#         try:
#             quantity = int(quantity)
#             reorder_level = int(reorder_level)
#             unit_price = float(unit_price)
#         except ValueError:
#             messages.error(request, "Please enter valid numbers for quantity, reorder level, and unit price.")
#             return redirect('add_item')

#         # ✅ Validation: No negative numbers
#         if quantity < 0:
#             messages.error(request, "Quantity cannot be negative.")
#             return redirect('add_item')

#         if reorder_level < 0:
#             messages.error(request, "Reorder level cannot be negative.")
#             return redirect('add_item')

#         if unit_price < 0:
#             messages.error(request, "Unit price cannot be negative.")
#             return redirect('add_item')

#         # Use custom category if "Other" is selected
#         final_category = custom_category if category == "Other" and custom_category else category

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

#     return render(request, 'inventory/add_item.html', {'PREDEFINED_CATEGORIES': ["Sensor", "Connector", "Resistor", "Microcontroller"]})

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
#         item.category = custom_category if category == "Other" and custom_category else category
#         item.quantity = quantity
#         item.reorder_level = reorder_level
#         item.unit_price = unit_price
#         item.supplier = supplier
#         item.location = location
#         item.description = description
#         item.save()

#         messages.success(request, "Item updated successfully!")
#         return redirect('inventory_list')

#     return render(request, 'inventory/edit_item.html', {'item': item, 'PREDEFINED_CATEGORIES': PREDEFINED_CATEGORIES})


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
#          # Create transaction and update timestamp
#         txn = Transaction.objects.create(item=item, transaction_type='IN', quantity=qty)
#         txn.date = timezone.now()  # ✅ manually update timestamp
#         txn.save()
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
#              # Create transaction and update timestamp
#             txn = Transaction.objects.create(item=item, transaction_type='OUT', quantity=qty)
#             txn.date = timezone.now()  # ✅ manually update timestamp
#             txn.save()
#             messages.success(request, f"{qty} units removed from {item.name}")
#         return redirect('inventory_list')
#     return render(request, 'inventory/remove_stock.html', {'item': item})


# def transaction_history(request):
#     # transactions = Transaction.objects.all().order_by('-date')
#     transactions = Transaction.objects.select_related('item').order_by('-date')
#     paginator = Paginator(transactions, 10)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     context = {
#         'transactions': transactions,
#         'PREDEFINED_CATEGORIES': PREDEFINED_CATEGORIES,
#         'page_obj': page_obj,
#     }
#     return render(request, 'inventory/transaction_history.html', context)

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Item, Transaction, Issuance
from django.db.models import F
from django.core.paginator import Paginator
from django.utils import timezone
from django.db import transaction
from .forms import IssuanceForm, ReceiveForm

# Predefined categories for dropdown
PREDEFINED_CATEGORIES = ["Sensor", "Connector", "Resistor", "Microcontroller"]


def dashboard(request):
    total_items = Item.objects.count()
    low_stock = Item.objects.filter(quantity__gt=0, quantity__lte=F('reorder_level')).count()
    out_stock = Item.objects.filter(quantity=0).count()
    items = Item.objects.all().order_by('serial_no')
    paginator = Paginator(items, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'total_items': total_items,
        'low_stock': low_stock,
        'out_stock': out_stock,
        'items': items,
        'PREDEFINED_CATEGORIES': PREDEFINED_CATEGORIES,
        'page_obj': page_obj,
    }
    return render(request, 'inventory/dashboard.html', context)


def inventory_list(request):
    items = Item.objects.all().order_by('serial_no')
    paginator = Paginator(items, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'items': items,
        'PREDEFINED_CATEGORIES': PREDEFINED_CATEGORIES,
        'page_obj': page_obj,
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

        try:
            quantity = int(quantity)
            reorder_level = int(reorder_level)
            unit_price = float(unit_price)
        except ValueError:
            messages.error(request, "Please enter valid numbers for quantity, reorder level, and unit price.")
            return redirect('add_item')

        if quantity < 0 or reorder_level < 0 or unit_price < 0:
            messages.error(request, "Negative values are not allowed.")
            return redirect('add_item')

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
        item.name = request.POST.get('name')
        category = request.POST.get('category')
        custom_category = request.POST.get('custom_category')
        item.category = custom_category if category == "Other" and custom_category else category
        item.quantity = request.POST.get('quantity')
        item.reorder_level = request.POST.get('reorder_level')
        item.unit_price = request.POST.get('unit_price')
        item.supplier = request.POST.get('supplier')
        item.location = request.POST.get('location')
        item.description = request.POST.get('description')
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
        txn = Transaction.objects.create(item=item, transaction_type='IN', quantity=qty)
        txn.date = timezone.now()
        txn.save()
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
            txn = Transaction.objects.create(item=item, transaction_type='OUT', quantity=qty)
            txn.date = timezone.now()
            txn.save()
            messages.success(request, f"{qty} units removed from {item.name}")
        return redirect('inventory_list')
    return render(request, 'inventory/remove_stock.html', {'item': item})


def transaction_history(request):
    transactions = Transaction.objects.select_related('item').order_by('-date')
    paginator = Paginator(transactions, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'transactions': transactions,
        'PREDEFINED_CATEGORIES': PREDEFINED_CATEGORIES,
        'page_obj': page_obj,
    }
    return render(request, 'inventory/transaction_history.html', context)


# ----------------------------- #
#     ISSUER PAGE SECTION       #
# ----------------------------- #

def issuance_list(request):
    """Display all issuances and provide issue/receive actions."""
    issuances = Issuance.objects.select_related('item').all().order_by('-issue_date')
    form = IssuanceForm()
    receive_form = ReceiveForm()
    return render(request, 'inventory/issuance_list.html', {
        'issuances': issuances,
        'form': form,
        'receive_form': receive_form,
    })


@transaction.atomic
def issue_item(request):
    """Handles issuing of components and deducts from stock."""
    if request.method != 'POST':
        return redirect('issuance_list')

    form = IssuanceForm(request.POST)
    if not form.is_valid():
        for err in form.errors.values():
            messages.error(request, err)
        return redirect('issuance_list')

    item = form.cleaned_data['item']
    qty = form.cleaned_data['quantity']

    # Lock item and update quantity safely
    item = Item.objects.select_for_update().get(pk=item.pk)
    if item.quantity < qty:
        messages.error(request, f"Not enough stock. Available: {item.quantity}")
        return redirect('issuance_list')

    Item.objects.filter(pk=item.pk).update(quantity=F('quantity') - qty)

    issuance = form.save(commit=False)
    issuance.issue_date = timezone.now()
    issuance.receive_date = None
    issuance.received = False
    issuance.save()

    messages.success(request, f"Issued {qty} × {item.name} successfully.")
    return redirect('issuance_list')


@transaction.atomic
def receive_item(request):
    """Handles return/receive of issued components."""
    if request.method != 'POST':
        return redirect('issuance_list')

    form = ReceiveForm(request.POST)
    if not form.is_valid():
        for err in form.errors.values():
            messages.error(request, err)
        return redirect('issuance_list')

    issuance = get_object_or_404(Issuance, pk=form.cleaned_data['issuance_id'])
    if issuance.received:
        messages.warning(request, "This issuance has already been received.")
        return redirect('issuance_list')

    status = form.cleaned_data['component_status']
    remark = form.cleaned_data.get('remark', '')

    issuance.component_status = status
    issuance.receive_date = timezone.now()
    issuance.remark = remark
    issuance.received = True
    issuance.save()

    # Add stock back if OK or Faulty
    if status in ('ok', 'faulty'):
        Item.objects.filter(pk=issuance.item.pk).update(quantity=F('quantity') + issuance.quantity)

    messages.success(request, f"Issuance #{issuance.pk} marked received as {status.upper()}. Stock updated.")
    return redirect('issuance_list')
