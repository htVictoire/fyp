from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Board, Pins

@csrf_exempt
def etat_outputs(request, board_id):
    if request.method == 'GET':
        outputs = Pins.objects.filter(board__numero=board_id)
        output_states = {output.gpio: output.state for output in outputs}
        return JsonResponse(output_states)

@csrf_exempt
def handle_output_create(request):
    if request.method == 'POST':
        data = request.POST
        name = data.get('name')
        board_id = data.get('board')
        gpio = data.get('gpio')
        state = data.get('state')

        board, created = Board.objects.get_or_create(board_id=board_id)
        output, created = Output.objects.get_or_create(name=name, board=board, gpio=gpio, state=state)

        return JsonResponse({'result': 'success'})

