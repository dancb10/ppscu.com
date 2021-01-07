from django.shortcuts import render
from courses.models import Course
from courses.forms import CourseForm
from django.http import HttpResponseRedirect
from django.views.generic import DetailView, CreateView, ListView

# def course_detail(request, course_id):
#     course = Course.objects.get(id=course_id)
#     return render(request,'courses/course_detail.html',
#     {
#         'course': course,
#     })

class CourseDetailView(DetailView):
    model = Course

course_detail = CourseDetailView.as_view()

class CourseListView(ListView):
    model = Course
    queryset = Course.objects.prefetch_related('students')

course_list = CourseListView.as_view()


# def course_list(request):
#     courses = Course.objects.prefetch_related('students')
#     return render(request, 'courses/courses_list.html',
#     {
#       'courses': courses,
#     })

def course_add(request):
    if request.POST:
        form = CourseForm(request.POST)
        if form.is_valid():
            new_course = form.save()
            return HttpResponseRedirect(new_course.get_absolute_url())
    else:
        form = CourseForm()
    return render(request, 'courses/course_form.html', {
        'form': form,
    })
