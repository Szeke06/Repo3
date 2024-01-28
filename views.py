from django.shortcuts import render, redirect
from .models import game
from .forms import GameForm , TestForm


def allgames(request):
    AG = game.objects.all()
    return render(request,'screen.html',{'text':AG})


def nowa(request):
    form = GameForm(request.POST or None, request.FILES or None)
    Tform = TestForm(request.POST or None)
    if all((form.is_valid(),Tform.is_valid())):
        GAME=form.save(commit=False)
        testg=Tform.save()
        GAME.testg =testg


        #gamedic = {'id' :G.id,'name': G.name , 'date' : str(G.date), 'playersnr' : str(G.playersnr) }
        #gamedic = {'MODEL' :G}
        #request.session['moje_dane']= gamedic
       # return redirect(Nposition)
    return  render(request, 'newGame.html', {"new": form})


def Nposition(request):
    #Tu juz zmieniłem z poprzedniej metody bo instancji nie przezucało ale nie działa :P
    game_data = request.session.get('MODEL', {})
    game_data.save()

"""
NO a tu podjełem probe wyświetlenia  i dopisania do instancji tych poł ale brakuje elementu self bo mi tej instancji nie przeżuclio ale udalo mi sie same jej dane przeżucic :)

    Number = (game_data.get('playersnr'))
    for i in  Number:
        Tform = TestForm
        game.testg = Tform
        game.save()
    return render(request,'newGame1.html',{"Tnew":Tform})


"""