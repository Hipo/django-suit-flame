from django import template
from django.conf import settings
from firebase_token_generator import create_token

register = template.Library()

@register.simple_tag
def check_flame_autosave():
    return settings.FLAME_AUTOSAVE

@register.simple_tag
def get_flame_subdomain():
    return settings.FLAME_FIREBASE_SUBDOMAIN

@register.simple_tag
def get_flame_token(uid):
    token = create_token(settings.FLAME_FIREBASE_SECRET_KEY, {"uid": str(uid)})

    return token

@register.simple_tag
def get_flame_secret_key():
    return settings.FLAME_FIREBASE_SECRET_KEY


# settings.py
# FLAME_AUTOSAVE = True
# FLAME_FIREBASE_SUBDOMAIN = 'https://scorching-inferno-9092.firebaseio.com'
# FLAME_FIREBASE_SECRET_KEY = 'z8lbA3KOIX9tZg9lmoWyi1sg8dL8uwOg8UxRyflO'