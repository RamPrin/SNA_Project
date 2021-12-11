from django import template

register = template.Library()


def navbar_item_tag(context, *args, **kwargs):
    return kwargs


register.inclusion_tag('blog/snippets/navbar_item.html', takes_context=True)(navbar_item_tag)
