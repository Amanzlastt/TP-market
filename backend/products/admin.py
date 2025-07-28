from django.contrib import admin
from .models import User, Product

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """
    **Objective**: Customize how User model appears in Django admin
    **Key Concepts**:
    - list_display: Fields to show in the list view
    - search_fields: Fields to search by
    - readonly_fields: Fields that can't be edited
    """
    list_display = ['username', 'email','first_name','last_name', 'date_joined']
    search_fields = ['email', 'first_name', 'last_name']
    readonly_fields = ['date_joined']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    **Objective**: Customize how Product model appears in Django admin
    **Key Concepts**:
    - list_display: Fields to show in the list view
    - list_filter: Add filters in the sidebar
    - search_fields: Fields to search by
    """
    list_display = ['name', 'type', 'price', 'created_at']
    list_filter = ['type', 'created_at']
    search_fields = ['name']
    