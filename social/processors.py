from .models import link

def ctx_dict(request):
    ctx= {}
    links=link.objects.all()
    for vari in links:
        ctx[vari.key]=vari.url
    return ctx