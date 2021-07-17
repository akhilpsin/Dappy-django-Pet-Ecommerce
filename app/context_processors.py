from . models import Cat

def menu_links(request):
    links= Cat.objects.all()
    return dict(links=links)