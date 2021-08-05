from django import template


register = template.Library()  # если мы не зарегистрируем наши фильтры, то Django никогда не узнает, где именно их искать и фильтры потеряются\


@register.filter(name='get_item')
def get_item(dictionary, key):
    return dictionary.get(key)
