from django.db.models import TextChoices


class RegionsChoices(TextChoices):
    CHUI = "chui", "Чуйская область"
    TALAS = "talas", "Таласская область"
    NARYN = "naryn", "Нарынская область"
    ISSYK_KUL = "issykkul", "Иссык-Кульская область"
    JALAL_ABAD = "jalalabad", "Джалал-Абадская область"
    OSH = "osh", "Ошская область"
    BATKEN = "batken", "Баткенская область"
