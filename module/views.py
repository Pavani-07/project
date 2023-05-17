from django.shortcuts import render, redirect
from BTExamStaffDB.models import BTStudentInfo

def index(request):
    return render(request,'index.html')

def stuhome(request):
    if request.method == 'POST':
        RegNo = request.POST.get('RegNo')
        try:
            student = BTStudentInfo.objects.get(RegNo=RegNo)
        except BTStudentInfo.DoesNotExist:
            context = {'error': 'Invalid RegNo'}
            return render(request, 'stuhome.html', context)
        else:
            request.session['student_id'] = student.RegNo
            return redirect('stupage')
    else:
        return render(request, 'stuhome.html')

def teachome(request):
    return render(request,'teachome.html')

def stupage(request):
    student_id = request.session.get('student_id')
    if not student_id:
        return redirect('stuhome')

    student = BTStudentInfo.objects.get(RegNo=student_id)
    #student_courses = StudentCourse.objects.filter(student=student)
    #student_honor_courses = StudentHonorCourse.objects.filter(student=student)

def teacpage(request):
    return render(request,'teacpage.html')