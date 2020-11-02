from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist, SuspiciousOperation, PermissionDenied
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils import timezone

from apps.aluno.models import Aluno
from apps.votacao.models import Votacao


# Create your views here.


def aluno_login(request):
    response = HttpResponse()
    try:
        if request.method == "POST":
            aluno_cpf = request.POST.get("alunoCpf")
            aluno_mat = request.POST.get("alunoMat")

            aluno = Aluno.objects.get(cpf=aluno_cpf)
            if not aluno.ja_votou:
                try:
                    User.objects.get(username=aluno.cpf)
                except:
                    pass
                finally:
                    User.objects.create_user(
                        username=aluno_cpf,
                        password=aluno_mat,
                        first_name='Aluno'
                    )

                user = authenticate(request, username=aluno.cpf, password=aluno_mat)
                login(request, user)
                return redirect('votar')
            else:
                print('ENTROU AQUI')
                raise PermissionDenied
        else:
            return render(request, 'votacao/login.html')
    except ObjectDoesNotExist:
        response = render(request, 'votacao/404.html')
    except SuspiciousOperation:
        response = render(request, 'votacao/hmmm.html')
    except PermissionDenied:
        response = render(request, 'votacao/403.html')
    finally:
        return response


def votacao_page(request):
    response = HttpResponse()
    try:
        user = request.user
        data = Votacao.objects.all()

        if user.username in ('ejrgeek', 'saymon@dce', 'visita@dce'):
            response = render(request, 'votacao/index.html', {'data': data})
            return response

        aluno = Aluno.objects.get(cpf=user.username)
        if aluno.ja_votou:
            raise PermissionDenied
        response = render(request, 'votacao/index.html', {'data': data})
        return response
    except ObjectDoesNotExist:
        response = render(request, 'votacao/404.html')
    except KeyError:
        response = render(request, 'votacao/hmmm.html')
    except PermissionDenied:
        response = render(request, 'votacao/403.html')
    finally:
        return response


def votar(request, numero):
    response = HttpResponse()
    try:
        user = request.user
        chapa = Votacao.objects.get(chapa__numero=numero)

        aluno = Aluno.objects.get(cpf=user.username)
        if aluno.ja_votou:
            raise PermissionDenied
        chapa.votos += 1
        chapa.save()
        aluno.ja_votou = True
        aluno.save()
        user = User.objects.get(username=user)
        user.delete()
        response = render(request, 'votacao/fim.html')
        return response
    except ObjectDoesNotExist:
        response = render(request, 'votacao/404.html')
    except PermissionDenied:
        response = render(request, 'votacao/403.html')
    except Exception:
        response = render(request, 'votacao/hmmm.html')
    finally:
        return response


def zeresima(request):
    response = HttpResponse()
    try:
        user = request.user
        data = Votacao.objects.all()
        if user.is_staff:
            for voto in data:
                voto.votos = 0
                voto.save()
            response = render(request, 'votacao/zeresima.html', {'data': data, 'hora': timezone.now})
            return response
        response = render(request, 'votacao/index.html')
        return response
    except ObjectDoesNotExist:
        response = render(request, 'votacao/404.html')
    except PermissionDenied:
        response = render(request, 'votacao/403.html')
    except Exception:
        response = render(request, 'votacao/hmmm.html')
    finally:
        return response


def boletim_urna(request):
    response = HttpResponse()
    try:
        user = request.user
        data = Votacao.objects.all()
        if user.is_staff:
            response = render(request, 'votacao/bu.html', {'data': data, 'hora': timezone.now})
            return response
        response = render(request, 'votacao/index.html')
        return response
    except ObjectDoesNotExist:
        response = render(request, 'votacao/404.html')
    except PermissionDenied:
        response = render(request, 'votacao/403.html')
    except Exception:
        response = render(request, 'votacao/hmmm.html')
    finally:
        return response
