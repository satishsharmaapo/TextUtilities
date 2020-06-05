from django.http import HttpResponse
from django.shortcuts import render    # this is for render 

def index(request):     
    return render(request,"index.html")

def analyze(request):
    textcontent=request.GET.get('text','default')
    # print(request.GET.get('text','default'))
    param={'name':'analyzer','content': textcontent}
    # return render(request,"analyze.html",param)
    removepunc=request.GET.get('removepunc',"off")
    captitalizefirst=request.GET.get('captitalizefirst',"off")
    newlineremove=request.GET.get('newlineremove',"off")
    spaceremover=request.GET.get('spaceremover',"off")
    charcounter=request.GET.get('charcounter',"off")
    if (removepunc=="on"):
          punctuations='''()-[]{};:'"\,<>./?@#$%^&*_~`'''
          data=""
          for char in textcontent:
              if char not in punctuations:
                  data=data+char
          params={"name":"Remove Punctuations","content":data}
          return render(request,'analyze.html',params)
    elif (captitalizefirst=="on"):           
          data=""
          for char in textcontent:               
                data=data+char.upper()
          params={"name":"Capitalize Punctuations","content":data}
          return render(request,'analyze.html',params)
    elif (newlineremove=="on"):           
          data=""
          for char in textcontent:
            if(char!="\n" and char!="\r"):
                  data=data+char
          params={"name":"newlineremove","content":data}
          return render(request,'analyze.html',params)
    elif (spaceremover=="on"):           
          data=""
          for index,char in enumerate(textcontent):             
            if not(textcontent[index]==" " and textcontent[index+1]==" "):
                  data=data+char
          params={"name":"spaceremover","content":data}
          return render(request,'analyze.html',params)
    elif (charcounter=="on"):           
          data=0
          for char in  textcontent:             
            if char != " " and char !="\n" and char!="\r" :
                  data+=1
          params={"name":"spaceremover","content":data}
          return render(request,'analyze.html',params)
    else:
        pass

    #     <input type="checkbox" name="removepunc">Remove punctutation</input>
    #     <input type="checkbox" name="captitalizefirst">captilization</input>
    #     <input type="checkbox" name="newlineremove">new Liner remover</input>
    #     <input type="checkbox" name="spaceremover">Space Remover</input>
    #     <input type="checkbox" name="charcounter">character count</input>
        

  
 

 