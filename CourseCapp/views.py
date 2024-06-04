from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Feature
from .models import Section1, Section2, Section3, Section4, results, COMUD
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Room, Message
# Create your views here.
def index(request):
    

    return render(request, 'index.html')

def counter(request):

    return render(request, 'counter.html')

def register(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        request.session['email'] = email

        if User.objects.filter(email = email).exists():
            messages.info(request,"Email already used")
            return redirect('register')
        else:
            user = User.objects.create_user(username=username,email=email,password=password)
            user.save();
            return redirect('quest1')

    return render(request,'register.html')

def login(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']

        request.session['un'] = username

        user = auth.authenticate(username = username, password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('dashboard')
        else:
            messages.info(request,'Credentials invalid')
            return redirect('login')
    else:
        return render(request, 'login.html')
    
def intro(request):
    return render(request, 'intro.html')

def dashboard(request):
    username = request.session['un']

    user = User.objects.get(username = username)

    email = user.email

    comud = COMUD.objects.get(email = email)

    O1C = comud.Option1C
    O1D = comud.Option1D
    O1B = comud.Option1B
    O1P = comud.Option1P

    O2C = comud.Option2C
    O2D = comud.Option2D
    O2B = comud.Option2B
    O2P = comud.Option2P

    O3C = comud.Option3C
    O3D = comud.Option3D
    O3B = comud.Option3B
    O3P = comud.Option3P

    
    return render(request, 'dashboard.html', {
        'name': username,
        'email': email,
        'O1C': O1C,
        'O1D': O1D,
        'O1B': O1B,
        'O1P': O1P,
        'O2C': O2C,
        'O2D': O2D,
        'O2B': O2B,
        'O2P': O2P,
        'O3C': O3C,
        'O3D': O3D,
        'O3B': O3B,
        'O3P': O3P,})


def first(request):
    request.session['s1'] = 0
    request.session['s2'] = 0
    request.session['s3'] = 0
    request.session['s4'] = 0
    return render(request, 'first.html')

def second(request):
    s1 = request.session['s1']
    s2 = request.session['s2']
    s3 = request.session['s3']
    s4 = request.session['s4']

    s1+=1
    return render(request, 'second.html',{'s1':s1})


def quest1(request):
    request.session['s1'] = 0
    request.session['s2'] = 0
    request.session['s3'] = 0
    request.session['s4'] = 0
    sect = Section1.objects.get(pk=1)
    answer = sect.answer
    quest = sect.quest

    request.session['email'] = request.session['email']
    
    return render( request, 'quest1.html',{'answer': answer, 'quest':quest, 'email': request.session['email']})

def quest2(request):
    if request.method == 'POST':
        request.session['s1'] = request.session['s1']
        request.session['s2'] = request.session['s2']
        request.session['s3'] = request.session['s3']
        request.session['s4'] = request.session['s4']

        request.session['email'] = request.session['email']

        

        value = request.POST['ANS']

        if(value == '2'):
           request.session['s1'] +=1

        sect = Section1.objects.get(pk=2)
        answer = sect.answer
        quest = sect.quest

        return render(request, 'quest2.html',{'answer': answer, 'quest':quest, 'value': request.session['s1']})

        
def quest3(request):
     if request.method == 'POST':
        request.session['s1'] = request.session['s1']
        request.session['s2'] = request.session['s2']
        request.session['s3'] = request.session['s3']
        request.session['s4'] = request.session['s4']

        request.session['email'] = request.session['email']

        

        value = request.POST['ANS']

        if(value == '3'):
           request.session['s1'] +=1

        sect = Section1.objects.get(pk=3)
        answer = sect.answer
        quest = sect.quest

        return render(request, 'quest3.html',{'answer': answer, 'quest':quest, 'value': request.session['s1']})
     
def quest4(request):
    if request.method == 'POST':
        request.session['s1'] = request.session['s1']
        request.session['s2'] = request.session['s2']
        request.session['s3'] = request.session['s3']
        request.session['s4'] = request.session['s4']
        request.session['email'] = request.session['email']

        

        value = request.POST['ANS']

        if(value == '3'):
           request.session['s1'] +=1

        sect = Section1.objects.get(pk=4)
        answer = sect.answer
        quest = sect.quest

        return render(request, 'quest4.html',{'answer': answer, 'quest':quest, 'value': request.session['s1']})

def quest5(request):
     if request.method == 'POST':
        request.session['s1'] = request.session['s1']
        request.session['s2'] = request.session['s2']
        request.session['s3'] = request.session['s3']
        request.session['s4'] = request.session['s4']
        request.session['email'] = request.session['email']

        

        value = request.POST['ANS']

        if(value == '3'):
           request.session['s1'] +=1

        sect = Section2.objects.get(pk=1)
        answer = sect.answer
        quest = sect.quest

        return render(request, 'quest5.html',{'answer': answer, 'quest':quest, 'value': request.session['s1']})
     
def quest6(request):
     if request.method == 'POST':
        request.session['s1'] = request.session['s1']
        request.session['s2'] = request.session['s2']
        request.session['s3'] = request.session['s3']
        request.session['s4'] = request.session['s4']
        request.session['email'] = request.session['email']

        

        value = request.POST['ANS']

        if(value == '3'):
           request.session['s2'] +=1

        sect = Section2.objects.get(pk=2)
        answer = sect.answer
        quest = sect.quest

        return render(request, 'quest6.html',{'answer': answer, 'quest':quest, 'value': request.session['s1'], 'value2': request.session['s2']})
     
def quest7(request):
    if request.method == 'POST':
        request.session['s1'] = request.session['s1']
        request.session['s2'] = request.session['s2']
        request.session['s3'] = request.session['s3']
        request.session['s4'] = request.session['s4']
        request.session['email'] = request.session['email']

        

        value = request.POST['ANS']

        if(value == '3'):
           request.session['s2'] +=1

        sect = Section2.objects.get(pk=3)
        answer = sect.answer
        quest = sect.quest

        return render(request, 'quest7.html',{'answer': answer, 'quest':quest, 'value': request.session['s1'], 'value2': request.session['s2']})
    
def quest8(request):
    if request.method == 'POST':
        request.session['s1'] = request.session['s1']
        request.session['s2'] = request.session['s2']
        request.session['s3'] = request.session['s3']
        request.session['s4'] = request.session['s4']
        request.session['email'] = request.session['email']

        

        value = request.POST['ANS']

        if(value == '1'):
           request.session['s2'] +=1

        sect = Section2.objects.get(pk=4)
        answer = sect.answer
        quest = sect.quest

        return render(request, 'quest8.html',{'answer': answer, 'quest':quest, 'value': request.session['s1'], 'value2': request.session['s2']})

def quest9(request):
    if request.method == 'POST':
        request.session['s1'] = request.session['s1']
        request.session['s2'] = request.session['s2']
        request.session['s3'] = request.session['s3']
        request.session['s4'] = request.session['s4']
        request.session['email'] = request.session['email']

        

        value = request.POST['ANS']

        if(value == '3'):
           request.session['s2'] +=1

        sect = Section3.objects.get(pk=1)
        answer = sect.answer
        quest = sect.quest

        return render(request, 'quest9.html',{'answer': answer, 'quest':quest, 'value': request.session['s1'], 'value2': request.session['s2'], 'value3': request.session['s3']} )

def quest10(request):
    if request.method == 'POST':
        request.session['s1'] = request.session['s1']
        request.session['s2'] = request.session['s2']
        request.session['s3'] = request.session['s3']
        request.session['s4'] = request.session['s4']
        request.session['email'] = request.session['email']

        

        value = request.POST['ANS']

        if(value == '3'):
           request.session['s3'] +=1

        sect = Section3.objects.get(pk=2)
        answer = sect.answer
        quest = sect.quest

        return render(request, 'quest10.html',{'answer': answer, 'quest':quest, 'value': request.session['s1'], 'value2': request.session['s2'], 'value3': request.session['s3']} )

def quest11(request):
    if request.method == 'POST':
        request.session['s1'] = request.session['s1']
        request.session['s2'] = request.session['s2']
        request.session['s3'] = request.session['s3']
        request.session['s4'] = request.session['s4']
        request.session['email'] = request.session['email']

        

        value = request.POST['ANS']

        if(value == '3'):
           request.session['s3'] +=1

        sect = Section3.objects.get(pk=3)
        answer = sect.answer
        quest = sect.quest

        return render(request, 'quest11.html',{'answer': answer, 'quest':quest, 'value': request.session['s1'], 'value2': request.session['s2'], 'value3': request.session['s3']} )
    
def quest12(request):
    if request.method == 'POST':
        request.session['s1'] = request.session['s1']
        request.session['s2'] = request.session['s2']
        request.session['s3'] = request.session['s3']
        request.session['s4'] = request.session['s4']
        request.session['email'] = request.session['email']

        

        value = request.POST['ANS']

        if(value == '1'):
           request.session['s3'] +=1

        sect = Section3.objects.get(pk=4)
        answer = sect.answer
        quest = sect.quest

        return render(request, 'quest12.html',{'answer': answer, 'quest':quest, 'value': request.session['s1'], 'value2': request.session['s2'], 'value3': request.session['s3']} )

def quest13(request):
    if request.method == 'POST':
        request.session['s1'] = request.session['s1']
        request.session['s2'] = request.session['s2']
        request.session['s3'] = request.session['s3']
        request.session['s4'] = request.session['s4']
        request.session['email'] = request.session['email']

        

        value = request.POST['ANS']

        if(value == '3'):
           request.session['s3'] +=1

        sect = Section4.objects.get(pk=1)
        answer = sect.answer
        quest = sect.quest

        return render(request, 'quest13.html',{'answer': answer, 'quest':quest, 'value': request.session['s1'], 'value2': request.session['s2'], 'value3': request.session['s3']} )

def quest14(request):
    if request.method == 'POST':
        request.session['s1'] = request.session['s1']
        request.session['s2'] = request.session['s2']
        request.session['s3'] = request.session['s3']
        request.session['s4'] = request.session['s4']
        request.session['email'] = request.session['email']

        

        value = request.POST['ANS']

        if(value == '2'):
           request.session['s4'] +=1

        sect = Section4.objects.get(pk=2)
        answer = sect.answer
        quest = sect.quest

        return render(request, 'quest14.html',{'answer': answer, 'quest':quest, 'value': request.session['s1'], 'value2': request.session['s2'], 'value3': request.session['s3']} )

def quest15(request):
    if request.method == 'POST':
        request.session['s1'] = request.session['s1']
        request.session['s2'] = request.session['s2']
        request.session['s3'] = request.session['s3']
        request.session['s4'] = request.session['s4']
        request.session['email'] = request.session['email']

        

        value = request.POST['ANS']

        if(value == '3'):
           request.session['s4'] +=1

        sect = Section4.objects.get(pk=3)
        answer = sect.answer
        quest = sect.quest

        return render(request, 'quest15.html',{'answer': answer, 'quest':quest, 'value': request.session['s1'], 'value2': request.session['s2'], 'value3': request.session['s3']} )

def quest16(request):
    if request.method == 'POST':
        request.session['s1'] = request.session['s1']
        request.session['s2'] = request.session['s2']
        request.session['s3'] = request.session['s3']
        request.session['s4'] = request.session['s4']
        request.session['email'] = request.session['email']

        

        value = request.POST['ANS']

        if(value == '1'):
           request.session['s4'] +=1

        sect = Section4.objects.get(pk=4)
        answer = sect.answer
        quest = sect.quest

        return render(request, 'quest16.html',{'answer': answer, 'quest':quest, 'value': request.session['s1'], 'value2': request.session['s2'], 'value3': request.session['s3']} )


def semiresult(request):
    if request.method == 'POST':
        request.session['s1'] = request.session['s1']
        request.session['s2'] = request.session['s2']
        request.session['s3'] = request.session['s3']
        request.session['s4'] = request.session['s4']
        request.session['email'] = request.session['email']

        

        value = request.POST['ANS']

        if(value == '4'):
           request.session['s4'] +=1 #16th question result calculation


        return render(request, 'semiresult.html')
    


def result(request):
    s1 = request.session['s1']
    s2 = request.session['s2']
    s3 = request.session['s3']
    s4 = request.session['s4']

    email = request.session['email']



    value = request.POST['ANS'] # personal preference question answer

    avg = int((s1+s2+s3+s4)/4)

    dict = {'s1': s1, 's2': s2, 's3': s3, 's4': s4}

    max = 0
    best = 'a'
    for a in dict:
        if max < dict[a]:
            max = dict[a]
            best = a

    option1 = results.objects.get(pk=1)
    C1 = option1.career
    D1=option1.description
    B1=option1.best_course
    P1 = option1.prospects


    option2 = results.objects.get(pk=2)
    C2 = option2.career
    D2=option2.description
    B2=option2.best_course
    P2 = option2.prospects

    option3 = results.objects.get(pk=3)
    C3 = option3.career
    D3=option3.description
    B3=option3.best_course
    P3 = option3.prospects


    if(best =='s1'):
        option1 = results.objects.get(pk=1)
        C1 = option1.career
        D1=option1.description
        B1=option1.best_course
        P1 = option1.prospects
    elif(best == 's2'):
        option1 = results.objects.get(pk=2)
        C1 = option1.career
        D1=option1.description
        B1=option1.best_course
        P1 = option1.prospects
    elif(best == 's3'):
        option1 = results.objects.get(pk=3)
        C1 = option1.career
        D1=option1.description
        B1=option1.best_course
        P1 = option1.prospects
    else:
        option1 = results.objects.get(pk=4)
        C1 = option1.career
        D1=option1.description
        B1=option1.best_course
        P1 = option1.prospects
        



    remove = dict.pop(best)


    max = 0
    best = 'a'
    for a in dict:
        if max < dict[a]:
            max = dict[a]
            best = a


    if(best =='s1'):
        option3 = results.objects.get(pk=1)
        C3 = option3.career
        D3=option3.description
        B3=option3.best_course
        P3 = option3.prospects
    elif(best == 's2'):
        option3 = results.objects.get(pk=2)
        C3 = option3.career
        D3=option3.description
        B3=option3.best_course
        P3 = option3.prospects
    elif(best == 's3'):
        option3 = results.objects.get(pk=3)
        C3 = option3.career
        D3=option3.description
        B3=option3.best_course
        P3 = option3.prospects
    else:
        option3 = results.objects.get(pk=4)
        C3 = option3.career
        D3=option3.description
        B3=option3.best_course
        P3 = option3.prospects



    if(value ==1):
        option2 = results.objects.get(pk=1)
        C2 = option2.career
        D2=option2.description
        B2=option2.best_course
        P2 = option2.prospects
    elif(value == 2):
        option2 = results.objects.get(pk=2)
        C2 = option2.career
        D2=option2.description
        B2=option2.best_course
        P2 = option2.prospects
    elif(value == 3):
        option2 = results.objects.get(pk=3)
        C2 = option2.career
        D2=option2.description
        B2=option2.best_course
        P2 = option2.prospects
    elif(value ==4):
        option2 = results.objects.get(pk=4)
        C2 = option2.career
        D2=option2.description
        B2=option2.best_course
        P2 = option2.prospects


    
    comud = COMUD.objects.create(
        email=email,
        Option1C = C1, 
        Option1D = D1, 
        Option1B = B1, 
        Option1P = P1,
        Option2C = C2, 
        Option2D = D2, 
        Option2B = B2, 
        Option2P = P2,
        Option3C = C3, 
        Option3D = D3, 
        Option3B = B3, 
        Option3P = P3,
        )
    comud.save();
    
    return render(request, 'result.html', {
        'C1': C1,
        'D1': D1,
        'B1': B1,
        'P1': P1,
        'C2': C2,
        'D2': D2,
        'B2': B2,
        'P2': P2,
        'C3': C3,
        'D3': D3,
        'B3': B3,
        'P3': P3,
        'avg': avg,
        
    })

def chathome(request):
    return render(request, 'chathome.html')


def chatroom(request, room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    return render(request, 'chatroom.html', {
        'username': username,
        'room': room,
        'room_details': room_details
    })

def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']

    if Room.objects.filter(name = room).exists():
        return redirect('/'+room+'/?username='+username)
    else:
        new_room = Room.objects.create(name = room)
        new_room.save()
        return redirect('/'+room+'/?username='+username)
    
def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()

    return HttpResponse('Message sent successfully')

def getMessages(request, room):
    room_details = Room.objects.get(name=room)

    messages = Message.objects.filter(room = room_details.id)
    return JsonResponse({"messages": list(messages.values())})