from django.contrib import admin
from .models import Category,Product

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)

    def save_model(self, request, obj, form, change):
        """Override save_model to ensure unique category names."""
        if not change:  # If creating a new category
            if Category.objects.filter(name=obj.name).exists():
                self.message_user(request, "Category name already exists.", level=admin.ERROR)
                return
        super().save_model(request, obj, form, change)

    def delete_model(self, request, obj):
        """Override delete_model to handle category deletions."""
        super().delete_model(request, obj)
        self.message_user(request, f"Category '{obj.name}' has been deleted.", level=admin.SUCCESS)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product)

