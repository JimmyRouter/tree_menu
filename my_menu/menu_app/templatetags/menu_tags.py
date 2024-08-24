from django import template
from django.urls import resolve

from menu_app.models import MenuItem

register = template.Library()


@register.inclusion_tag('site_menu.html', name='draw_menu', takes_context=True)
def draw_menu(context: template.context.RequestContext, menu_name: str = None):
    try:
        menu = MenuItem.objects.prefetch_related('children').get(menu_name=menu_name)
        return {
            'menu': menu,
            'status': 'on' if context.request.__dict__['path_info']
                              and (menu.url == context.request.__dict__['path_info']
                                   or menu.named_url == context.request.__dict__['resolver_match'].url_name) else 'off',
        }
    except Exception as e:
        print('Exception in menu_tags draw_menu:>>', e)
        return {
            'menu': {
                'title': 'Error loading menu',
                'url': '#',
            },
            'status': 'on',
        }
