from django.shortcuts import render, get_object_or_404
from .models import Item, Category

# Vista para la página principal
def home(request):
    # Filtra los artículos que no han sido vendidos
    items = Item.objects.filter(is_sold=False)
    categories = Category.objects.all()

    # Contexto con los datos a pasar a la plantilla
    context = {
        'items': items,
        'categories': categories
    }

    # Renderiza la vista de inicio con los datos proporcionados
    return render(request, 'store/home.html', context)  # Ajusta la ruta si es necesario

# Vista para el detalle del artículo
def detail(request, pk):
    # Obtén el artículo con el id (pk) proporcionado
    item = get_object_or_404(Item, pk=pk)
    
    # Encuentra artículos relacionados que no estén vendidos y excluye el actual
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[:3]

    # Contexto con los datos del artículo y los relacionados
    context = {
        'item': item,
        'related_items': related_items
    }

    # Renderiza la vista del detalle con los datos proporcionados
    return render(request, 'store/item.html', context)