from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
transcript_list = [
    {'id': '1',
     'name': 'Kwame Benqazy',
     'class': 'Form2',
     'grade': 'First Class'
     },
    {'id': '2',
     'name': 'Fella Kuti',
     'class': 'Form3',
     'grade': 'First Class'
     },
    {'id': '3',
     'name': 'J. Cole',
     'class': 'Form1',
     'grade': 'Second Class'
     },
]


def transcripts(request):
    page = "transcripts"
    context = {
        'page': page,
        'transcripts': transcript_list,
    }
    return render(request, 'transcripts/transcripts.html', context)


def transcript(request, pk):
    transcript_obj = None
    for i in transcript_list:
        if i['id'] == pk:
            transcript_obj = i
    return render(request, 'transcripts/single-transcript.html', {'transcript': transcript_obj})
