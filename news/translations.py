"""UI Translation strings for different languages"""

TRANSLATIONS = {
    'uz': {
        'login': 'Kirish',
        'signup': 'Ro\'yxatdan o\'tish',
        'logout': 'Chiqish',
        'username': 'Foydalanuvchi nomi',
        'password': 'Parol',
        'email': 'Email',
        'add_article': 'Maqola qo\'shish',
        'welcome': 'Xush kelibsiz',
        'settings': 'Sozlamalar',
        'profile': 'Profil',
        'search': 'Qidirish',
        'categories': 'Kategoriyalar',
    },
    'ru': {
        'login': 'Вход',
        'signup': 'Регистрация',
        'logout': 'Выход',
        'username': 'Имя пользователя',
        'password': 'Пароль',
        'email': 'Email',
        'add_article': 'Добавить статью',
        'welcome': 'Добро пожаловать',
        'settings': 'Настройки',
        'profile': 'Профиль',
        'search': 'Поиск',
        'categories': 'Категории',
    },
    'en': {
        'login': 'Login',
        'signup': 'Sign Up',
        'logout': 'Logout',
        'username': 'Username',
        'password': 'Password',
        'email': 'Email',
        'add_article': 'Add Article',
        'welcome': 'Welcome',
        'settings': 'Settings',
        'profile': 'Profile',
        'search': 'Search',
        'categories': 'Categories',
    },
}


def get_translation(language, key, default=''):
    """Get translated string for a key and language"""
    return TRANSLATIONS.get(language, {}).get(key, default)
