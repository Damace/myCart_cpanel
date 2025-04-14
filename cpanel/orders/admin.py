from django.contrib import admin
from .models import Order,OrderItem,Payment,ItemReview,Offer
from .models import ProductOrders


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('client', 'status', 'created_at', 'created_at')
    search_fields = ('client__full_name', 'status')
    list_filter = ('status', 'created_at')


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'price', 'product_name')
    search_fields = ('product__name', 'order__id')
    list_filter = ('order__status',)

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('order', 'payment_method', 'payment_date')
    search_fields = ('order__id', 'payment_method')
    list_filter = ('payment_method', 'payment_date')


@admin.register(ItemReview)
class ItemReviewAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'customer', 'rating', 'comments_date')
    list_filter = ('rating', 'comments_date')
    search_fields = ('product_name', 'customer', 'phone_number')
    ordering = ('-comments_date',)


@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ('product', 'discount_percentage', 'start_date', 'end_date', 'created_at')
    search_fields = ('product__name', 'discount_percentage')
    list_filter = ('start_date', 'end_date', 'created_at')
    ordering = ('-created_at',)
    date_hierarchy = 'start_date'


@admin.register(ProductOrders)
class ProductOrdersAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'phone_number', 'quantity', 'price', 'total_cost', 'order_status', 'payment_status','receipt_number','order_date_time')
    list_filter = ('order_status', 'payment_status','order_date_time')
    search_fields = ('product_name', 'phone_number')
    ordering = ('-order_date_time',)
    readonly_fields = (
        'total_cost',
        'order_date_time'  # Makes order date and time readonly
    )

    fields = (
        'product_image',  # Include product_image in the editable fields
        'product_name',
        'phone_number',
        'quantity',
        'price',
        'total_cost',
        'order_status',
        'payment_status',
    )

    def get_readonly_fields(self, request, obj=None):
        """
        Makes `total_cost` field readonly for both creation and updates.
        """
        if obj:  # Editing an existing object
            return self.readonly_fields + ('product_name', 'phone_number', 'price', 'quantity')
        return self.readonly_fields


