from datacenter.models import *
import random
import logging

def fix_marks(schoolkid_name):
    schoolkids = Schoolkid.objects.filter(full_name__contains=schoolkid_name)
    if len(schoolkids) > 1:
        logging.error("Найдено больше одного ученика, содержащего такое имя. Завершение работы.")
        return
    elif len(schoolkids) < 1:
        logging.error("Не найдено ни одного ученика, содержащего такое имя. Завершение работы.")
        return
    schoolkid = schoolkids[0]
    marks = Mark.objects.filter(
        schoolkid=schoolkid,
        points__in=[2, 3]
    )
    for mark in marks:
        mark.points = 5
        mark.save()
        print(mark.points)

def remove_chastisements(schoolkid_name):
    schoolkids = Schoolkid.objects.filter(full_name__contains=schoolkid_name)
    if len(schoolkids) > 1:
        logging.error("Найдено больше одного ученика, содержащего такое имя. Завершение работы.")
        return
    elif len(schoolkids) < 1:
        logging.error("Не найдено ни одного ученика, содержащего такое имя. Завершение работы.")
        return
    schoolkid = schoolkids[0]
    chastisements = Chastisement.objects.filter(schoolkid=schoolkid)
    for chastisement in chastisements:
        chastisement.delete()

def create_commendation(schoolkid_name, subject_title):
    commendations = [
        "Хвалю!",
        "Молодец!",
        "Отлично!",
        "Хорошо!",
        "Великолепно!",
        "Очень хороший ответ!",
        "Cущественно лучше!",
        "Так держать!",
        "С каждым разом у тебя получается всё лучше!",
        "Я вижу, как ты стараешься!",
        "Я поражен!",
        "Прекрасное начало!"
    ]
    schoolkids = Schoolkid.objects.filter(full_name__contains=schoolkid_name)
    if len(schoolkids) > 1:
        logging.error("Найдено больше одного ученика, содержащего такое имя. Завершение работы.")
        return
    elif len(schoolkids) < 1:
        logging.error("Не найдено ни одного ученика, содержащего такое имя. Завершение работы.")
        return
    schoolkid = schoolkids[0]
    lesson = Lesson.objects.filter(subject__title=subject_title).last()
    commendation = Commendation.objects.create(
        subject=lesson.subject,
        teacher=lesson.teacher,
        created=lesson.date,
        text=random.choice(commendations),
        schoolkid_id=schoolkid.id
    )