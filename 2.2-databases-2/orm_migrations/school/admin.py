from django.contrib import admin

from .models import Student, Teacher


class MentoringInline(admin.StackedInline):
    model = Student.teacher.through
    extra = 1

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    inline = [
        MentoringInline,
    ]


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    inline = [
        MentoringInline,
    ]
