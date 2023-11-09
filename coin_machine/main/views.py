from django.http import JsonResponse
from django.shortcuts import render
from .forms import MachineParams
from .logic.coin_machine import CoinMachine
from .logic.fraction import Fraction
from django.core.exceptions import BadRequest

# Create your views here.
def index(request):
    form = MachineParams()
    context = {"form": form}
    return render(request, "index.html", context)


def get_machine(request):
    machine = CoinMachine(
        
        int(request.GET.get('coin_number')),\
        int(request.GET.get('exits_to_continue')),\
        int(request.GET.get('exits_event_happened')))
    return machine


def flip_a_coin(request):
    machine = get_machine(request)
    result = machine.conduct()
    return JsonResponse({'result':result})


def get_probability(request):
    machine = get_machine(request)
    number = int(request.GET.get('number'))
    if (number <= 0):
        return JsonResponse({'result':'error'})

    result = machine.try_experiments(number)
    return JsonResponse({'result':result})



def machine_view(request):
    try:
        machine = CoinMachine(
            
            int(request.GET.get('coin_number')),\
            int(request.GET.get('exits_to_continue')),\
            int(request.GET.get('exits_event_happened')))
        
        context = {'description': machine.description(),\
                'coin_number': int(request.GET.get('coin_number')),\
                'exits_to_continue': int(request.GET.get('exits_to_continue')),\
                'exits_event_happened':int(request.GET.get('exits_event_happened')),\
                'probability': str(machine.probability_by_formula()),\
                'probability_decimal' : str(machine.probability_by_formula().decimal())}
        return render(request, "machine.html", context)
    except ValueError:
        raise BadRequest("Such coin machine is not valid")
    

def handler400(request, exception, template_name="bad_request.html"):
    context = {'msg' : exception}
    return render(request, template_name, context)
