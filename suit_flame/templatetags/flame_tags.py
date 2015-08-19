from django import template
from django.conf import settings
from firebase_token_generator import create_token

register = template.Library()

@register.simple_tag
def check_flame_autosave():
    return settings.FLAME_AUTOSAVE

@register.simple_tag
def get_flame_subdomain():
    """
    Returns the firebase subdomain from settings.

    Example:
        FLAME_FIREBASE_SUBDOMAIN = 'https://scorching-inferno-136.firebaseio.com'

    """
    return settings.FLAME_FIREBASE_SUBDOMAIN

@register.simple_tag
def get_flame_token(uid):
    """
    Creates a public key using the user id and the secret key.
    FLAME_FIREBASE_SECRET_KEY = 'z22bA3KOg54gfwr9lmoWyi1sg8dL8uwOg8txRyfl2'
    """
    token = create_token(settings.FLAME_FIREBASE_SECRET_KEY, {"uid": str(uid)})
    return token
