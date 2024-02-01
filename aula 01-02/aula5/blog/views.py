from django.shortcuts import render
from django.http import HttpResponseRedirect

def feed(request):
    context = {
        'posts': [
            {'author': 'Fulano', 'date': '01/02/24', 'content': 'aksajslajlsjalkslkjaksjalkjsfb'},
            {'author': 'Beltrano', 'date': '01/02/24', 'content': 'çalspclpflvr5484eowpijnsim'},
            {'author': 'Ciclano', 'date': '01/02/24', 'content': 'a51s6516de81d6e8aksjaosn12817unslka'}
        ]
    }
    return render(request, 'feed.html', context)

def publicate(request):
    if request.method == 'POST':
        author = request.POST.get("author"),
        content = request.POST.get("content")
        print(author)
        print(content)
        return HttpResponseRedirect('/feed')
    else:
        return render(request, 'publicate.html')