# مشروع لتنفيذ وادخال عددين كليين وإجراء العمليات الحسابية عليهما
# الخوارمية تخص الاعداد الكلية فقط حالياً
# يمكن تطوير المشروع بتعديل الخوارزمية وتطويرها لتشمل كل صيغ الاعداد الممكنة


def calc(x, y):  # تعريف الدالة
    print(':', 'النتيجة ')
    print(x, '+', y, '=', x + y)  # ناتج الجمع
    print(x, '-', y, '=', x - y)  # ناتج الطرح
    print(x, '*', y, '=', x * y)  # ناتج الضرب
    # -----ناتج القسمة--------
    if y !=0 : print(x, '/', y, '=', x / y)
    else : print('القسمة على صفر كمية غير معرفة')
    # -------نهاية القسمة------
    print("مربع العدد",x,'=',x**2)#الاسس او القوى نستخدم دائماً نجمتين للتعبير عنها
    print("الجذر التربيعي للعدد",y, '=', round(y ** 0.5,3))#تم استخدام دالة round لتقريب العدد الناتج لأقرب جزء من ألف

def enter_number_and_check(x):#دالة ادخال العددين وتحمل قيمة الأول أو الثاني اشارة الى ترتيب العدد
    number=0
    ok=False
    wrong=False
    while not ok: #يستمر loop حتى يدخل المستخدم عدد صحيحاً
        if not wrong:
            print('ادخل العدد', x)  # نطلب من المستخدم ادخال اول عدد
        else:
            print('اعد ادخال العدد',x,'بشكل صحيح')

        try:
          number=int(input(''))  # يدخل المستخدم العدد الأول
          ok = True #عندما يدخل المستخدم عدد تتحول القيمة هنا لtrue وبذلك ينتهي ال loop

        except ValueError:
            wrong=True # عند الفيمة true تظهر للمستخدم رسالة اعادة ادخال العدد
            continue # استمرار ال loop حتى يتم تصحيح ادخال المستخدم لعدد صحيح

    return number # قمة ارجاع الدالة وهي العدد المدخل بشكل صحيح



print('----Start App-----')  # للإعلان عن بداية تنفذ الكود
x=enter_number_and_check("الأول") #ادخال العدد الأول والتحقق منه
y=enter_number_and_check("الثاني")#ادخال العدد الثاني والتحقق منه
calc(x,y)#بعد نجاح تنفيذ السطرين السابقين يتم تنفيذ دالة العمليات الحسابية
print('---- End App -----')  # للإعلان عن الانتهاء من تنفيذ الكود
