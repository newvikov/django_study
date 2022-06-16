from django.db import models

# Create your models here.
class Order(models.Model):
    order_dt = models.DateTimeField(auto_now=True)
    order_name = models.CharField(max_length=200, verbose_name= 'Имя') #добавляя verbose_name изменяем отобращение модели в проекте пользователю
    order_phone = models.CharField(max_length=200, verbose_name= 'Номер телефона')
    
    #отступы очень важны. ниже мы назначаем название ввиде имени для пользователей на портале. 
    def __str__(self):
        return self.order_name

    class Meta:
        verbose_name = 'Заказ' #для Order делаем перевод 
        verbose_name_plural = 'Заказы' #для множественного числа Order делаем перевод
     