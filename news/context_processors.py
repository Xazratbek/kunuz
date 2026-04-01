from .models import Category, CategoryTranslation

def categories(request):
    """Context processor to provide categories to all templates"""
    # Get language from URL or use default
    lang = 'uz'  # Default language

    # All categories
    all_categories = Category.objects.all().order_by('name')

    # Getting categories with translations
    navbar_cats = Category.objects.filter(parent__isnull=True).order_by('name')[:8]
    footer_cats = Category.objects.all().order_by('name')[:12]

    return {
        'categories': all_categories,
        'navbar_categories': navbar_cats,
        'footer_categories': footer_cats,
        'current_language': lang,
    }
