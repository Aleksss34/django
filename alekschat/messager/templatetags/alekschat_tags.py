from django import template
from messager.models import *
register = template.Library()
@register.simple_tag()#для простого тега
def get_categories(filter=None):
    if not filter:
        return Categories.objects.all()
    else:
        return Categories.objects.filter(filter)
@register.inclusion_tag('messager/teg.html')#для вывода html страницы
def show_categories(filter=None, cat_selected=0):#задать какой либо параметр для тега
    if not filter:
        cats = Categories.objects.all()
    else:
        cats = Categories.objects.filter(pk__gte=filter)


    return {'cats':cats, 'cat_selected': cat_selected}
@register.inclusion_tag('messager/posts.html')
def show_posts():
    posts = Messager.objects.all()
    return {'posts':posts,}