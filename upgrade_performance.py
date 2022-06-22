from datacenter.models import Schoolkid
from datacenter.models import Mark, Lesson
from datacenter.models import Chastisement, Commendation
import random
import logging


def fix_marks(schoolkid_name):
    schoolkid = get_schoolkid(schoolkid_name)
    marks = Mark.objects.filter(
        schoolkid=schoolkid,
        points__in=[2, 3]
    )
    for mark in marks:
        mark.points = 5
        mark.save()


def remove_chastisements(schoolkid_name):
    schoolkid = get_schoolkid(schoolkid_name)
    chastisements = Chastisement.objects.filter(schoolkid=schoolkid)
    chastisements.delete()


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
    schoolkid = get_schoolkid(schoolkid_name)
    lesson = Lesson.objects.filter(subject__title=subject_title).last()
    commendation = Commendation.objects.create(
        subject=lesson.subject,
        teacher=lesson.teacher,
        created=lesson.date,
        text=random.choice(commendations),
        schoolkid_id=schoolkid.id
    )

    def get_schoolkid(full_name):
        try:
            schoolkids = Schoolkid.objects.get(full_name__contains=full_name)
        except MultipleObjectsReturned:
            logging.error(
                "Найдено больше одного ученика, содержащего такое имя." /
                "Завершение работы."
            )
            return
        except DoesNotExist:
            logging.error(
                "Не найдено ни одного ученика, содержащего такое имя." /
                "Завершение работы."
            )
            return
        return schoolkid
