from django.shortcuts import render

# Create your views here.
from .models import *
import re








# Create your views here.
def index(request):
    list = []

    def replace():
        단어들 = 임시사전.objects.filter(id__gte=34325)
        for 단어 in 단어들:
            # print(단어)
            p = re.compile('[ ]+')
            m = p.search(단어.단어)
            if m:
                단어.delete()


            # try:
            #     n = m.group()
            #     if n not in list:
            #         list.append(n)
            # except: pass

    replace()

    print('list=',list)

    # for i in list:
    #     객체 = 임시사전(단어 = i)
    #     객체.save()


            # 단어.출처='자주쓰는한국어낱말'
            # 단어.save()
    #
    # def replace2():
    #     단어들 = 사전.objects.filter(id__gt=3721)
    #     print(len(단어들))
    #     for 단어 in 단어들:
    #         단어.delete()
    #
    # def archive():
    #     p = re.compile('.+적$')
    #     m = p.match(단어.단어)
    #     단어.save()


    return render(request, 'bnm/index.html')