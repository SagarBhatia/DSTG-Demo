from django.shortcuts import render

def demoGUI(request):
    return render(request, 'dstg_demo/index.html')