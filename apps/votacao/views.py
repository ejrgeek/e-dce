from django.core.exceptions import ObjectDoesNotExist, SuspiciousOperation, PermissionDenied
from django.shortcuts import render

from apps.aluno.models import Aluno
from apps.chapa.models import Chapa

# Create your views here.


def aluno_login(request):
    try:
        if request.method == "POST":
            aluno_cpf = str(request.POST.get("alunoCpf"))
            aluno_mat = str(request.POST.get("alunoMat"))
            aluno = Aluno.objects.get(cpf=aluno_cpf, matricula=aluno_mat)
            if not aluno.ja_votou:
                chapas = Chapa.objects.all()
                return render(request, 'votacao/index.html', {'data': chapas})
            else:
                raise PermissionDenied
        else:
            return render(request, 'votacao/404.html')
    except ObjectDoesNotExist:
        return render(request, 'votacao/404.html')
    except SuspiciousOperation:
        return render(request, 'votacao/hmmm.html')
    except PermissionDenied:
        return render(request, 'votacao/403.html')
