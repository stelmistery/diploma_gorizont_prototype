from django.db import models


# class Category(models.Model):
#     name = models.CharField(max_length=255, null=False, verbose_name='Название')
#     conditions = models.TextField(null=False, verbose_name='Условия')
#     price = models.IntegerField(null=False, verbose_name='Цена')
#
#     class Meta:
#         verbose_name = 'Категория'
#         verbose_name_plural = 'Категории'
#         ordering = ['price']
#
#
# class Room(models.Model):
#     room_number = models.AutoField(primary_key=True, versbose_name='Номер категории',)
#     category_id = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Номер категории')
#     number_of_place = models.IntegerField(null=False, verbose_name='Кол-во мест')
#
#     class Meta:
#         verbose_name = 'Комната'
#         verbose_name_plural = 'Команты'
#         ordering = ['room_number']
#
#
# class Book(models.Model):
#     Book_code = models.AutoField(primary_key=True, verbose_name='Код брони')
#     room_id = models.ForeignKey(Room, on_delete=models.CASCADE, verbose_name='Номер комнаты')
#     number_of_peaple = models.IntegerField(max_length=4, verbose_name='Кол-во жильцов', default=0)
#     date_of_arrival = models.DateField()
#
# class UserBook(models.Model):
#     book_id = models.ForeignKey(Book verbose_name='Номер брони')
#     user_id = models.ForeignKey()
#     phone = models.CharField(max_length=20, null=False, verbose_name='Номер телефона')
#
#     class Meta:
#         verbose_name = 'Список жителей'
#         verbose_name_plural = 'Списки жителей'
#         ordering = ['book_id']
#
#
# class