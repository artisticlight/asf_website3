def all_pages(request):
    from mezzanine.galleries.models import Gallery
    galleries = Gallery.objects.all()
    return {'pages': galleries}