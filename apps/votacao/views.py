from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist, SuspiciousOperation, PermissionDenied
from django.shortcuts import render, redirect
from django.utils import timezone

from apps.aluno.models import Aluno
from apps.votacao.models import Votacao


# Create your views here.


def aluno_login(request):
    try:
        if request.method == "POST":
            aluno_cpf = str(request.POST.get("alunoCpf"))
            aluno_mat = str(request.POST.get("alunoMat"))
            aluno = Aluno.objects.get(cpf=aluno_cpf, matricula=aluno_mat)
            if not aluno.ja_votou:
                if not User.objects.get(username=request.user.username):
                    User.objects.create_user(
                        username=aluno_cpf,
                        password=aluno_mat,
                        first_name='Aluno'
                    )
                user = authenticate(request, username=aluno.cpf, password=aluno_mat)
                login(request, user)
                return redirect('votar')
            else:
                raise PermissionDenied
        else:
            return render(request, 'votacao/login.html')
    except ObjectDoesNotExist:
        return render(request, 'votacao/404.html')
    except SuspiciousOperation:
        return render(request, 'votacao/hmmm.html')
    except PermissionDenied:
        return render(request, 'votacao/403.html')


def votacao_page(request):
    try:
        user = request.user
        data = Votacao.objects.all()

        if user.username in ('ejrgeek', 'saymon@dce', 'visita@dce'):
            return render(request, 'votacao/index.html', {'data': data})

        aluno = Aluno.objects.get(cpf=user)
        if aluno.ja_votou:
            raise PermissionDenied

        return render(request, 'votacao/index.html', {'data': data})
    except ObjectDoesNotExist:
        return render(request, 'votacao/404.html')
    except KeyError:
        return render(request, 'votacao/hmmm.html')
    except PermissionDenied:
        return render(request, 'votacao/403.html')


def votar(request, numero):
    try:
        user = request.user
        chapa = Votacao.objects.get(chapa__numero=numero)

        aluno = Aluno.objects.get(cpf=user)
        if aluno.ja_votou:
            raise PermissionDenied
        chapa.votos += 1
        chapa.save()
        aluno.ja_votou = True
        aluno.save()
        user = User.objects.get(username=user)
        user.delete()
        return render(request, 'votacao/fim.html')
    except ObjectDoesNotExist:
        return render(request, 'votacao/404.html')
    except PermissionDenied:
        return render(request, 'votacao/403.html')
    except Exception as e:
        print(e)
        return render(request, 'votacao/hmmm.html')


def zeresima(request):
    try:
        user = request.user
        data = Votacao.objects.all()
        if user.username in ('ejrgeek', 'saymon@dce', 'visita@dce'):
            for voto in data:
                voto.votos = 0
                voto.save()
            return render(request, 'votacao/zeresima.html', {'data': data, 'hora': timezone.now})

        return render(request, 'votacao/index.html')
    except ObjectDoesNotExist:
        return render(request, 'votacao/404.html')
    except PermissionDenied:
        return render(request, 'votacao/403.html')
    except Exception as e:
        print(e)
        return render(request, 'votacao/hmmm.html')


def boletim_urna(request):
    try:
        user = request.user
        data = Votacao.objects.all()
        if user.username in ('ejrgeek', 'saymon@dce', 'visita@dce'):
            return render(request, 'votacao/bu.html', {'data': data, 'hora': timezone.now})
        return render(request, 'votacao/index.html')
    except ObjectDoesNotExist:
        return render(request, 'votacao/404.html')
    except PermissionDenied:
        return render(request, 'votacao/403.html')
    except Exception as e:
        print(e)
        return render(request, 'votacao/hmmm.html')
