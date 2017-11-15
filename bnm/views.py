from django.shortcuts import render, get_object_or_404
from django.db.models import Q, Sum
from random import random

from .models import *
import re








# Create your views here.
def index(request):

    # def replace1():
    #     단어들 = 사전.objects.filter(Q(id__gte=20))
    #     for 단어 in 단어들:
    #         print(단어.단어)
    #         단어.출처='자주쓰는한국어낱말'
    #         단어.save()
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
    # replace1()

    return render(request, 'bnm/index.html')












def generate(request):

    # generate에 쓰이는 함수 tool들

    def n글자찾기(n):
        for 명사 in 사전.objects.filter(Q(품사='명사') & ~Q(품사2='지명') & Q(국적='한국어') & ~Q(Tag='순우리말1')).order_by('?'):
            if len(명사.단어) == n:
                return 명사.단어


    def 받침판단기(word):    ###유니코드 공식에 따라 단어의 마지막 글자 받침 유무 판단
        last = word[-1]
        criteria = (ord(last) - 44032) % 28
        if criteria == 0:
            return '와 '
        else:
            return '과 '


    def 장얼생성기():
        word3 = n글자찾기(3)
        word2 = n글자찾기(2)
        return word3+받침판단기(word3)+word2+'들'


    def 명명생성기():
        word1 = 사전.objects.filter(Q(품사='명사') & (Q(Tag='기본') | Q(Tag='한국어1') | Q(Tag='순우리말') | Q(Tag='외래어1'))).order_by('?').first().단어
        word2 = 사전.objects.filter(Q(품사='명사') & (Q(Tag='기본') | Q(Tag='한국어1') | Q(Tag='순우리말') | Q(Tag='외래어1'))).order_by('?').first().단어
        return word1+받침판단기(word1)+word2




    def 알고리즘선택기():  ###랜덤 숫자 3개 선택해서 Votes에 따라 weighted 방법에 의해 인기 많은 애들 위주로 알고리즘 골라줌
        rand = [random(), random(), random()]

        sum = Algorithm.objects.aggregate(value=Sum('Votes'))
        total = sum['value']

        selected_algorithms = []

        알고리즘들 = Algorithm.objects.all()
        for i in range(3):
            r = rand[i]
            this = 0
            for 알고리즘 in 알고리즘들:
                a = this / total
                this = this + 알고리즘.Votes
                b = this / total
                if a < r <= b:
                    selected_algorithms.append(알고리즘.이름)
                    break

        return selected_algorithms



    #본격 이름 생성!

    selected_algorithms = 알고리즘선택기()
    algorithms = Algorithm.objects.all()
    내용들=[]
    print(selected_algorithms)

    for i in range(3):
        for algorithm in algorithms:
            if algorithm.이름==selected_algorithms[i]:
                내용들.append(algorithm.내용)

    context = {'이름1':eval(내용들[0]), '이름2':eval(내용들[1]), '이름3':eval(내용들[2])}
    return render(request, 'bnm/generate.html', context)