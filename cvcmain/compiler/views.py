from django.shortcuts import render, redirect
from .models import register, questions,post,comment
from django.views.decorators.csrf import csrf_protect
from django.contrib import auth

op = ''


# Create your views here.

def check(c, i, l):
    global op
    import requests, json
    result_url = 'https://ide.geeksforgeeks.org/submissionResult.php'
    url = 'https://ide.geeksforgeeks.org/main.php'

    program = c
    inputs = i
    data = {
        'lang': l,
        'code': program,
        'input': inputs,
        'save': 'false'
    }
    r = requests.post(url=url, data=data)
    try:
        p = json.loads(r.text)['sid']
    except:
        op = 'Unknown Error'
        return 0

    data = {'sid': p,
            'requestType': 'fetchResults'}
    while 1:
        result = requests.post(url=result_url, data=data)

        if 'SUCCESS' in result.text:
            r = json.loads(result.text)
            try:
                op = r['output']
                break

            except:
                if 'rntError' in result.text:
                    r = json.loads(result.text)
                    op = 'Error ' + r['rntError']
                break


def index(request):
    global op
    if request.method == "POST":
        code = str(request.POST['code']).strip()
        ip = str(request.POST['input']).strip()
        lan = str(request.POST['lan']).strip()
        print(code, ip, lan)
        check(code, ip, lan)
        return render(request, 'compiler.html', {'op': op, 'ip': ip, 'code': code})
    else:
        return render(request, 'compiler.html', {'op': 'Output', 'ip': 'Inputs', 'code': 'Your Code here'})


def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def blog(request):
    return render(request, 'blog.html')


def registeruser(request):
    if request.method == "POST":

        name = request.POST['name']
        email = request.POST['email']
        mobile = request.POST['mobile']
        password = request.POST['password']
        if name != ' ' and email != '' and mobile != '' and password != '':
            data = register.objects.all()
            emails = []
            for d in data:
                emails.append(d.email)
            if email not in emails:
                registe = register(name=name, email=email, mobile=mobile, password=password, answers=0, answered=[0])
                registe.save()
                message = 'Registation Succesful'
            else:
                message = 'User already registered'
        else:

            message = 'Fill all Details'
        return render(request, 'index.html', {'message': message})
    else:
        message = False
        return render(request, 'index.html', {'message': message,'questions':len(questions.objects.all()),'students':len(register.objects.all())})


def login(request):
    email = request.POST['email']
    mail = email
    password = request.POST['password']
    if email != '' and password != " ":
        data = register.objects.all()
        emailspwds = {}
        for d in data:
            emailspwds[d.email] = d.password
        if emailspwds[email] == password:

            message = 'Login Succesful'
            return render(request, 'compiler.html', {'user': 'mail'})
        else:
            message = 'Login Failed'
    else:
        message = 'Fill all Details'

    return render(request, 'index.html', {'message': message})


def test(request):
    global name
    try:
        name = request.POST['email']
    except:
        name = ''
    t = register.objects.get(email=name)
    i = str(int(t.answers) + 1)
    global op
    try:
        questio = questions.objects.get(id=i)
    except:
        return render(request,'congo.html',{'user':t.name,'email':name})
    if request.method == "POST":
        try:
            code = str(request.POST['code']).strip()
            ip = str(request.POST['input']).strip()
            lan = str(request.POST['lan']).strip()
            check(code, ip, lan)
            print(questio.answer.strip(), op.strip())
            if questio.answer.strip() == op.strip():
                t = register.objects.get(email=name)
                ans = t.answered
                if str(i) not in str(ans):
                    t.answers = str(int(t.answers) + 1)
                    ans = ans + ' ' + str(i)
                    t.answered = ans
                    t.save()
                return render(request, 'compiler.html',
                              {'op': op, 'ip': ip, 'code': code, 'succes': True, 'user': name,'next':True,'question': questio.question})
        except:
            t = questions.objects.get(no=i)
            op = t.answer
            ip = t.inputs
            code = ''
            return render(request, 'compiler.html', {'op': op, 'ip': ip, 'code': code, 'succes': False, 'user': name,'question': questio.question})

        else:
            return render(request, 'compiler.html', {'op': op, 'ip': ip, 'code': code, 'succes': False, 'user': name,'question': questio.question})

    else:
        questio = questions.objects.all()
        # print(questio[i].question)
        return render(request, 'compiler.html',
                      {'op': questio.answer, 'ip': questio[i].inputs, 'code': 'Your Code here',
                       'question': questio.question, 'user': name})
def gg(request):
    posts1=(post.objects.all()[0:len(post.objects.all())/2])[::-1]
    posts2 = (post.objects.all()[len(post.objects.all()) / 2:])[::-1]
    return render(request,'test.html',{'posts1':posts2,'a':'0','posts2':posts1})

def show(request,pk):
    g=post.objects.get(id=pk)
    return render(request,'blog-single.html',{'img':g.img.url,'content':g.content,'title':g.title,'cat':g.cat,'date':g.date})

def team(request):
    return render(request,'teachers.html')

def contact(request):
    if request.method=="POST":

        fname=request.POST['first_name']
        lname = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        comments = request.POST['comments']
        if fname!=''and lname != '' and email != '' and phone != '' and comments != '':
            registe = comment(fname=fname,lname=lname,email=email,phone=phone,comments=comments)
            registe.save()
            sent=True
            message=' Message Sent Succesfully'
            return render(request,'contact.html',{'sent':sent,'message':message})
        else:
            sent = True
            message = 'Fill all Details'
            return render(request, 'contact.html', {'sent': sent, 'message': message})

    else:
        return render(request,'contact.html')