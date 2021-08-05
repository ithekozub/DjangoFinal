from .models import Post
from django.contrib.sites.models import Site


def site_name_render(request):
    return {
        'site_name': Site.objects.get_current().name,
    }


def cat_names_render(request):
    cat_names = {i.name: i.label for i in Post.Category}
    return {
        'cat_names': cat_names,
    }