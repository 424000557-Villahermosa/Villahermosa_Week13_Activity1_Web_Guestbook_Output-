from django.shortcuts import render, redirect
from .forms import EntryForm
from .models import Entry

def guestbook(request):
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('guestbook')
    else:
        form = EntryForm()

    entries = Entry.objects.order_by('-created_at')
    return render(request, 'guestbook.html', {'form': form, 'entries': entries})