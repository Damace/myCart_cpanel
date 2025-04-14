from django.contrib import admin

from product_management.models import Category, Product
from review_management.models import Review


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'rating','comment','created')
    search_fields = ('product__name', 'user__full_name')


admin.site.register(Review, ReviewAdmin)
