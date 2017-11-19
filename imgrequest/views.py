import subprocess
from django.http import JsonResponse


def handle_file(file):
    with open('./images/exit.jpg', 'wb+') as destination:
        for chunk in file.chunk():
            destination.write(chunk)


def check_exit():
    result = subprocess.run(['~/darknet/darknet detector test cfg/coco.data cfg/yolo.cfg yolo.weights '
                             './images/exit.jpg'], stdout=subprocess.PIPE)
    resultstr = result.stdout.decode('utf-8')
    if "exit" in resultstr:
        return True
    else:
        return False


def process_img(request):
    if request.method == 'POST':
        handle_file(request.FILES['file'])
    result = check_exit()
    return JsonResponse({'ServerResponseData': str(result)})


def index(request):
    return JsonResponse({'HelloWorld': 'HeyThere'})
