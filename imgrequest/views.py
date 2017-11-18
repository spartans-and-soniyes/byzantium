from django.shortcuts import render


def handle_file(file):
    with open('./images/exit.jpg', 'wb+') as destination:
        for chunk in file.chunk():
            destination.write(chunk)


def get_img(request):
    if request.method == 'POST':
        handle_file(request.FILES['file'])


