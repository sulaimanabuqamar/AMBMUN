from django.shortcuts import get_object_or_404, render
from .models import *
from itertools import groupby

def Home(request):
    board = Board.objects.all().order_by('-club', 'id')
    grouped_board = {}

    for club, members in groupby(board, key=lambda x: x.club):
        grouped_board[club] = list(members)

    return render(request, "index.html", {'grouped_board': grouped_board})

def Schedule(request):
    return render(request, "schedule.html")

def Rules(request):
    return render(request, "rules.html")

def Committees(request):
    chairs = Chair.objects.all()
    committees = Committee.objects.all()

    context = {
        'chairs': chairs,
        'committees': committees,
    }

    return render(request, 'committees.html', context)

def Committee_Detail(request, committee_id):
    committee = get_object_or_404(Committee, pk=committee_id)
    return render(request, 'committee_detail.html', {'committee': committee})

def About(request):
    return render(request, "about.html")

def Contact(request):
    board_members = Board.objects.filter(club=Board.Club.MUN)
    return render(request, "contact.html", {'board_members': board_members})

def Faq(request):
    questions = FAQ.objects.all()
    return render(request, "faq.html", {'questions': questions})
