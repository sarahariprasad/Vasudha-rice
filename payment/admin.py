from django.contrib import admin
import openpyxl
from django.http import HttpResponse
# Register your models here.

from django.contrib import admin
from .models import Order, OrderItem

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user','full_name','phone', 'order_date', 'total_amount', 'payment_method', 'is_paid', 'address', 'order_status')
    list_filter = ('is_paid', 'order_date')
    search_fields = ('user__username', 'id')
    list_editable = ('is_paid','order_status',)
    actions = ['download_orders_as_excel']

    def download_orders_as_excel(self, request, queryset):
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=orders.xlsx'

        workbook = openpyxl.Workbook()
        worksheet = workbook.active
        worksheet.title = 'Orders'

        columns = [
            'Order ID', 'User Email', 'Full Name', 'Phone', 'Order Date', 'Total Amount', 
            'Payment Method', 'Is Paid', 'Address', 'City', 'State', 'Post Code', 'Order Status'
        ]
        worksheet.append(columns)

        for order in queryset:
            order_date = order.order_date
            if order_date is not None and order_date.tzinfo is not None:
                order_date = order_date.replace(tzinfo=None)  # Remove timezone info
            
            row = [
                order.id, order.user.email, order.full_name, order.phone, order_date, 
                order.total_amount, order.payment_method, order.is_paid, order.address, 
                order.city, order.state, order.post_code, order.get_order_status_display()
            ]
            worksheet.append(row)

        workbook.save(response)
        return response

    download_orders_as_excel.short_description = "Download selected orders as Excel"



@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'quantity', 'price']
    list_filter = ('order', 'product')  # Adds an additional filter by product
    search_fields = ('order__id', 'product__name')  # Enables search by order ID and product name
    ordering = ('order',)  # Orders the list view by order
    actions = ['download_order_items_as_excel']


    def download_order_items_as_excel(self, request, queryset):
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=order_items.xlsx'

        workbook = openpyxl.Workbook()
        worksheet = workbook.active
        worksheet.title = 'Order Items'

        columns = [
            'Order ID', 'Product', 'Quantity', 'Price'
        ]
        worksheet.append(columns)

        for item in queryset:
            row = [
                item.order.id, item.product.title, item.quantity, item.price
            ]
            worksheet.append(row)

        workbook.save(response)
        return response

    download_order_items_as_excel.short_description = "Download selected order items as Excel"
