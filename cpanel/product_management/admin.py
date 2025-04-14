from django.contrib import admin # type: ignore
from .models import Category, Product
from django.contrib.auth.models import User, Group


class CustomUserAdmin(admin.ModelAdmin):
    # Customize User admin as needed
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('username', 'email')

class CustomGroupAdmin(admin.ModelAdmin):
    # Customize Group admin as needed
    list_display = ('name',)
    search_fields = ('name',)

# Unregister the default User and Group admin
admin.site.unregister(User)
admin.site.unregister(Group)

# Register custom admin classes
admin.site.register(User, CustomUserAdmin)
admin.site.register(Group, CustomGroupAdmin)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')  # Display 'name' and 'slug' columns in the admin list view
    prepopulated_fields = {'slug': ('name',)}  # Automatically populate the slug field based on the 'name'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'stock', 'available','orders','image','image2','image3','created', 'updated')
    #list_filter = ('available', 'created', 'updated', 'category')  # Add filter options
    list_editable = ('price', 'stock', 'available', 'orders')  # Make fields editable directly in the list view
    prepopulated_fields = {'slug': ('name',)}  # Automatically populate the slug field based on the 'name'
    search_fields = ('name', 'description')  # Enable search functionality for 'name' and 'description' fields



# admin.site.register(Product, ProductAdmin)
# admin.site.register(Category, CategoryAdmin)

from django.contrib import admin
from .models import ProductReview

@admin.register(ProductReview)
class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'customer', 'comments_date')  # Fields to display in admin list view
    search_fields = ('product_name', 'customer')  # Enable search by product name and customer
    list_filter = ('comments_date',)  # Add filter for comments_date

from django.contrib import admin
from .models import Supplier

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('supplier_name', 'supplier_phone', 'supplier_address')
    search_fields = ('supplier_name', 'supplier_phone')