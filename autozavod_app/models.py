from django.db import models

# Create your models here.


class EVP_CLASS(models.Model):

    name_evp_class = models.CharField(
        max_length=10, null=True, blank=True
    )  # EVP-Class доступа

    def __str__(self):
        return self.name_evp_class



    

class Section(models.Model):

    section = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.section or "Не существует"
    
class Workshop(models.Model):

    workshop_name = models.CharField(max_length=10, null=True, blank=True)
    
    def __str__(self):
        return self.workshop_name


class Action(models.Model):
    action_name = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.action_name or "Не существует"


class TypeDoc(models.Model):

    type_name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.type_name or "Без имени"


class Stuff(models.Model):

    ON_LEAVE_CHOICES = [
        ("SVO", "СВО"),
        ("DEC", "Декрет"),
    ]

    name = models.CharField(max_length=50, blank=True)  # ФИО
    position = models.CharField(max_length=100, null=True, blank=True)  # Позиция
    evp_class = models.ManyToManyField(
        EVP_CLASS, blank=True, verbose_name="Группа ознакомления"
    )
    workshop = models.ForeignKey(
        Workshop, on_delete=models.SET_NULL, null=True, blank=True
    )  # К какому цеху прикреплён
    section = models.ForeignKey(Section, on_delete=models.SET_NULL, null=True, blank=True) # Отдел
    id_number = models.IntegerField(null=True, blank=True)  # Табельный номер сотрудника
    status = models.BooleanField(default=True)  # Статус сотрудника работает\нет
    on_leave = models.CharField(
        max_length=3, choices=ON_LEAVE_CHOICES, null=True, blank=True
    )  # Временное отсутсвие СВО\Декрет

    def __str__(self):
        return f"{self.name} (№{self.id_number})" if self.id_number else self.name


class Process(models.Model):

    STATUS_CHOICES = [
    (True, "Да"),
    (False, "Нет"),
    (None, "Неизвестно"),
]

    action = models.ManyToManyField(
        Action, max_length=200, blank=True, verbose_name="Действие"
    )
    type = models.ForeignKey(
        TypeDoc, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Тип"
    )
    name_doc = models.CharField(
        max_length=100, null=True, blank=True, verbose_name="Название документа"
    )
    responsible_process = models.ManyToManyField(
        Stuff, blank=True, verbose_name="Ответственные"
    )
    date_deadline = models.DateField(
        blank=True, null=True, verbose_name="Срок выполнения"
    )
    release_date = models.DateField(null=True, blank=True, verbose_name="Дата загрузки")
    status_procces = models.BooleanField(
    null=True,
    blank=True,
    choices=STATUS_CHOICES,
    verbose_name="Статус выполнения",
    default='False'
    )
    comment = models.TextField(
        max_length=40, blank=True, null=True, verbose_name="Комментарий"
    )
    link = models.FileField(
        upload_to="autozavod_app/media",
        null=True,
        blank=True,
        verbose_name="Загрузка документа",
    )

    @property
    def status_display(self):
        return "Да" if self.status else "Нет"
    
    def __str__(self):
        actions = ", ".join([str(action) for action in self.action.all()])
        return f"{actions}"


class Orders(models.Model):

    GROUP_CHOICES = [
        ("ПБ", "Пожарная безопасность"),
        ("ПР", "Промышленная безопасность"),
        ("ОТ", "Охрана труда"),
        ("ЭК", "Экология"),
        ("HR", "HR"),
    ]

    ARCHIVE_CHOICES = [
        ("Y", "Действующий"),
        ("N", "Архив"),
    ]

    name = models.CharField(max_length=100, null=True, blank=True)
    id_doc = models.CharField(max_length=20, null=True, blank=True)
    workshop = models.ManyToManyField(Workshop, blank=True, verbose_name="Цех")
    group = models.CharField(
        max_length=2,
        choices=GROUP_CHOICES,
        null=True,
        blank=True,
        verbose_name="Направление",
    )
    evp_class = models.ManyToManyField(
        EVP_CLASS, blank=True, verbose_name="Группа ознакомления"
    )
    release_date = models.DateField(blank=True, null=True, verbose_name="Дата выпуска")
    mayor = models.ManyToManyField(Stuff, blank=True, verbose_name="Ответственные")
    responsible_not = models.ManyToManyField(
        Stuff,
        blank=True,
        verbose_name="Не ознакомлены",
        related_name="responsible_orders",
    )
    responsible = models.ManyToManyField(
        Stuff,
        blank=True,
        verbose_name="Ознакомлены",
        related_name="responsible_not_orders",
    )
    process = models.ManyToManyField(
        Process, blank=True, verbose_name="Действия к распоряжению"
    )
    status = models.CharField(
        max_length=1,
        choices=ARCHIVE_CHOICES,
        verbose_name="Статус приказа",
        default="Y",
    )
    link = models.FileField(
        upload_to="autozavod_app/media",
        null=True,
        blank=True,
        verbose_name="Загрузка документа",
    )

    def __str__(self):
        return self.name if self.name else "Без имени"


class Doc(models.Model):

    ACTUAL_CHOICES = [
        ("Y", "Актуален"),
        ("N", "Не актуален"),
    ]

    ARCHIVE_CHOICES = [
        ("Y", "Действующий"),
        ("N", "Архив"),
    ]

    GROUP_CHOICES = [
        ("ПБ", "Пожарная безопасность"),
        ("ПР", "Промышленная безопасность"),
        ("ОТ", "Охрана труда"),
        ("ЭК", "Экология"),
        ("HR", "HR"),
    ]

    name = models.CharField(max_length=100, null=True, blank=True, verbose_name="Имя")
    id_doc = models.CharField(
        max_length=100, null=True, blank=True, verbose_name="id документа"
    )
    type_doc = models.ManyToManyField(TypeDoc, verbose_name="Тип документа", blank=True)
    mayor = models.ManyToManyField(Stuff, blank=True, verbose_name="Ответственные")
    responsible_not = models.ManyToManyField(
        Stuff, blank=True, verbose_name="Не ознакомлены", related_name="responsible"
    )
    responsible = models.ManyToManyField(
        Stuff, blank=True, verbose_name="Ознакомлены", related_name="responsible_not"
    )
    status = models.CharField(
        max_length=1, choices=ARCHIVE_CHOICES, verbose_name="Статус приказа"
    )
    actual = models.CharField(
        max_length=1,
        choices=ACTUAL_CHOICES,
        null=True,
        blank=True,
        verbose_name="Актуальность",
    )
    group = models.CharField(
        max_length=2,
        choices=GROUP_CHOICES,
        null=True,
        blank=True,
        verbose_name="Направление",
    )
    workshop = models.ManyToManyField(Workshop, blank=True, verbose_name="Цех")
    evp_class = models.ManyToManyField(
        EVP_CLASS, blank=True, verbose_name="Группа ознакомления"
    )
    date = models.DateField(blank=True, null=True, verbose_name="Дата выпуска")
    process = models.ManyToManyField(
        Process, blank=True, verbose_name="Действия к приказу"
    )
    orders = models.ManyToManyField(Orders, blank=True, verbose_name="Распоряжения")
    comment = models.TextField(max_length=40, blank=True, null=True)
    link = models.FileField(
        upload_to="autozavod_app/media", null=True, verbose_name="Загрузка документа"
    )

    

    def __str__(self):
        return self.name if self.name else "Без имени"
