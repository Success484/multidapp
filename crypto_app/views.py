from django.shortcuts import render
from .models import Multiapps
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def homePage(request):
    search_query = request.GET.get('q', '')
    if search_query:
        all_apps = Multiapps.objects.filter(name__icontains=search_query)
    else:
        all_apps = Multiapps.objects.all()
    page_obj=paginate_objects(request, all_apps, 24)
    context = {
        'page_obj': page_obj,
        'search_query': search_query,
    }
    return render(request, 'main/index.html', context)


def appDetail(request, app_id):
    app = get_object_or_404(Multiapps, id=app_id)
    return render(request, 'main/detail.html', {'app':app})


def paginate_objects(request, object_list, items_per_page):
    paginator = Paginator(object_list, items_per_page)
    page_number = request.GET.get("page")
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    
    return page_obj