from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import render


@login_required
def course_chat_room(request, course_id):
    try:
        # Извлекаем курс с заданным ID, к которому присоединился текущий пользователь
        course = request.user.courses_joined.get(id=course_id)
    except:
        # Пользователь не является студентом курса, либо курс не существует
        return HttpResponseForbidden()
    return render(request, 'chat/room.html', {'course': course})
