#المشروع الثاني وهو تبسط الكسور الاعتيادية
#الخوارزمية تختص بالاعداد الطبيعية فقط
#يمكن توسيع الخوارزمية لتشمل الاعداد الحقيقية
#تطوير الخوارزمية ثم الكود هو تحدي لمتابعينا الكرام

def enter_and_check():
    print('ادخل كسرا على صورة a/b لتبسيطه')
    frac=input()
    while '/' not in frac:  #عند عدم ادخال المسخدم رمز القسمة يطلب منه اعادة الادخال
        print('اكتب كسراً بالصيغة a/b')
        frac=input()
        continue

    return frac.split('/')#إرجاع لستة تحوي البسط والمقام على الترتيب

def simplify(list):
    a=int(list[0])
    b=int(list[1])
    factors=[]
    max_factor=1
    if a < b:
        if b % a == 0:
            print(a,'/',b,'=','1','/',int(b/a))
            return
        for i in range(1,round(a+1)):
            if a % i == 0:
                factors.append(i)
        for j in factors:
            if b % j==0:
                max_factor=j
        if max_factor==1:print("لايمكن التبسيط فهو مبسط بأبسط صورة")
        else:print(a,'/',b,'=',int(a/max_factor),'/',int(b/max_factor))
    elif a>b:
        if a%b==0:
            print(a, '/', b, '=',int(a / b ))
            return
        for i in range(1, b+1):
            if b % i == 0:
                factors.append(i)
        for j in factors:
            if a % j == 0:
                max_factor = j
        if max_factor == 1:print("لايمكن التبسيط فهو مبسط بأبسط صورة")
        else:print(a, '/', b, '=',int(a / max_factor), '/',int(b / max_factor))
    else:
        print(a, '/', b, '=','1')





print('------بداية التطبيق------')
fraction=enter_and_check()#وضع قيمة المتغير fraction مساوياً لقيمة الدالة التي ترجع list
simplify(fraction)#استدعاء دالة التبسيط مع تمرير list تحوي البسط والمقام
print('------نهاية التطبيق------')
