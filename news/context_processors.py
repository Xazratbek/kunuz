from .models import Category, CategoryTranslation
from .translations import TRANSLATIONS, get_translation
from django.utils.translation import get_language

def categories(request):
    """Context processor to provide categories and translations to all templates"""
    # Get current language from request
    current_lang = get_language() or 'uz'

    # Ensure language is valid
    if current_lang not in TRANSLATIONS:
        current_lang = 'uz'

    # All categories
    all_categories = Category.objects.all().order_by('name')

    # Getting categories with translations
    navbar_cats = Category.objects.filter(parent__isnull=True).order_by('name')[:8]
    footer_cats = Category.objects.all().order_by('name')[:12]

    return {
        'categories': all_categories,
        'navbar_categories': navbar_cats,
        'footer_categories': footer_cats,
        'current_language': current_lang,
        'translations': TRANSLATIONS.get(current_lang, {}),
        'available_languages': [
            {'code': 'uz', 'name': 'O\'zbekcha', 'short': 'O\'z'},
            {'code': 'ru', 'name': 'Ruscha', 'short': 'Ru'},
            {'code': 'en', 'name': 'Inglizcha', 'short': 'En'},
        ],
    }
