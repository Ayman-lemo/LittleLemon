from django.shortcuts import render

def index(request):
    # دالة render تقوم بدمج الطلب مع ملف HTML وتعرضه للمستخدم
    return render(request, 'index.html', {})