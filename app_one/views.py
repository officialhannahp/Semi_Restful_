from django.shortcuts import render, redirect
from.models import Show
from django.contrib import messages

def root(request):
    return redirect('/shows')

def show(request):
    context = {
        "shows" : Show.objects.all()
    }
    return render(request, "shows.html", context)

def new(request):
    return render(request, "new.html")

def create(request):

    errors =  Show.objects.basic_validator(request.POST)

    if len(errors) > 0:
        for k, v in errors.items():
            messages.error(request, v)
        return redirect('/shows/new')

    else:
        print(request.POST)
        new_show = Show.objects.create(
            title=request.POST['title'],
            network=request.POST['network'],
            release_date=request.POST['date'],
            desc=request.POST['desc']
        )
        return redirect(f'/shows/{new_show.id}')

def show_info(request, show_id):
    show = Show.objects.get(id=show_id)
    context = {
        'show' : show,
    }
    return render(request, "show_info.html", context)

def edit(request, show_id):
    shows = Show.objects.get(id=show_id)
    context = {
        "show" : shows
    }
    return render(request, "edit.html", context)

def update(request, show_id):

    errors =  Show.objects.basic_validator(request.POST)

    if len(errors) > 0:
        for k, v in errors.items():
            messages.error(request, v)
        return redirect('/shows/new')

    else:
        show = Show.objects.get(id=show_id)
        show.title = request.POST['title']
        show.network = request.POST['network']
        show.release_date = request.POST['date']
        show.desc = request.POST['desc']
        show.save()
        return redirect(f'/shows/{show_id}')

def destroy(request, show_id):
    show = Show.objects.get(id=show_id)
    show.delete()
    return redirect('/shows')