from django.contrib import admin
from .models import Order, StatusCrm, ComentCrm

# Register your models here.
class Coment(admin.StackedInline):
    model = ComentCrm
    fields = ('coment_dt', 'coment_text')
    readonly_fields = ('coment_dt',)
    extra = 1 #отвечает за количество полей для коментарив
class OrderAdm(admin.ModelAdmin):
    list_display = ('id', 'order_status', 'order_name', 'order_phone', 'order_dt') #выводит дополнительные колонки с данныеми в таблцу отображения
    list_display_links = ('id', 'order_name') #делает кликабельным опредленные поля
    search_fields = ('id', 'order_name', 'order_phone', 'order_dt')
    list_filter = ('order_status',) #запятая обязательная, не будет без нее работать т.к. это кортеж
    list_editable =('order_status', 'order_phone')
    list_per_page = 10
    list_max_show_all = 100
    fields = ('id', 'order_status', 'order_dt', 'order_phone')
    readonly_fields = ('id', 'order_dt')
    #поле класса комент
    inlines = [Coment,] #по умолчанию будет выводить три поля для коментов

admin.site.register(Order, OrderAdm)
admin.site.register(StatusCrm)
admin.site.register(ComentCrm)
 