from django.contrib import admin
from .models import Category_Hoel, Room_Info, Customer_Info, Room_Use, Service, Book_Room
# Register your models here.
class CategoryHoelAdmin(admin.ModelAdmin):
    list_display = ('CategoryCode','CategoryName')
    search_fields = ['CategoryName']
    list_filter = ('CategoryCode','CategoryName')
admin.site.register(Category_Hoel, CategoryHoelAdmin)

class RoomInfoAdmin(admin.ModelAdmin):
    list_display = ('RoomCode','KindOfRoom','Price','Status','RoomTel','CategoryCode')
    search_fields = ['KindOfRoom']
    list_filter = ('RoomCode','KindOfRoom','Price','Status','RoomTel','CategoryCode')
admin.site.register(Room_Info,RoomInfoAdmin)

class CustomerInfoAdmin(admin.ModelAdmin):
    list_display = ('CustomerCode','FullName','CustomerTel','CCCD')
    search_fields = ['FullName']
    list_filter = ('CustomerCode','FullName','CustomerTel','CCCD')
admin.site.register(Customer_Info,CustomerInfoAdmin)

class RoomUseAdmin(admin.ModelAdmin):
    list_display = ('CustomerCode','RoomCode')
    search_fields = ['RoomCode']
    list_filter = ('CustomerCode','RoomCode')
admin.site.register(Room_Use,RoomUseAdmin)

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('ServiceCode','ServiceName','UnitPrice')
    search_fields = ['ServiceName']
    list_filter = ('ServiceCode','ServiceName','UnitPrice')
admin.site.register(Service,ServiceAdmin)

class BookRoomAdmin(admin.ModelAdmin):
    list_display = ('CustomerCode','RoomCode','ReceivedDate')
    search_fields = ['ReceivedDate']
    list_filter =  ('CustomerCode','RoomCode','ReceivedDate')
admin.site.register(Book_Room,BookRoomAdmin)