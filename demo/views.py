from django.shortcuts import render, redirect
import language_tool_python
# Create your views here.
def hello(request):
   return render(request, "demo/home.html",{})

def res(request):
   b = request.POST['txt']
   tool = language_tool_python.LanguageTool('en-US')
   txt = tool.correct(b)
   return render(request, "demo/home.html" ,{'inp':b,'txt':txt})