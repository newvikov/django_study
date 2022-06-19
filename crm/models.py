from django.db import models

# Create your models here.
class StatusCrm(models.Model):
    Status_name = models.CharField(max_length=200, verbose_name='Название статуса')

    def __str__(self):
        return self.Status_name

    class Meta:
        verbose_name = 'Статус' 
        verbose_name_plural = 'Статусы'


class Order(models.Model):
    order_dt = models.DateTimeField(auto_now=True)
    order_name = models.CharField(max_length=200, verbose_name= 'Имя') #добавляя verbose_name изменяем отобращение модели в проекте пользователю
    order_phone = models.CharField(max_length=200, verbose_name= 'Номер телефона')
    order_status = models.ForeignKey(StatusCrm, on_delete=models.PROTECT, null=True, blank=True, verbose_name='Статус') #класс статус становиться родителем. поле становится привязкой, 

    #отступы очень важны. ниже мы назначаем название ввиде имени для пользователей на портале. 
    def __str__(self):
        return self.order_name

    class Meta:
        verbose_name = 'Заказ' #для Order делаем перевод 
        verbose_name_plural = 'Заказы' #для множественного числа Order делаем перевод

class ComentCrm(models.Model):
    coment_binding = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name= 'Заявка')
    coment_text = models.TextField(verbose_name= 'Текст комментария')
    coment_dt = models.DateTimeField(auto_now=True, verbose_name='Дата создания')
    
    def __str__(self):
        return self.coment_text

    class Meta:
        verbose_name = 'Комментарий' 
        verbose_name_plural = 'Комментарии'