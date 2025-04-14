from django.contrib import admin
from .models import MembershipType, Member

@admin.register(MembershipType)
class MembershipTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'duration_months')
    search_fields = ('name',)
    list_filter = ('duration_months',)

# @admin.register(Member)
# class MemberAdmin(admin.ModelAdmin):
#     list_display = ('client', 'membership_type', 'start_date', 'end_date', 'active')
#     search_fields = ('client__full_name', 'membership_type__name')
#     list_filter = ('active',)


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    # Display these fields in the admin list view
    list_display = (
        'phone_number',
        'name',
        'membership_type',
        'price',
        'duration',
        'start_date',
        'end_date',
        'active',
    )

    # Add filters for fields
    list_filter = (
        'membership_type',
        'start_date',
        'end_date',
        'active',
    )

    # Searchable fields
    search_fields = (
        'phone_number',
        'name',
        'membership_type__name',
    )

    # Fieldsets for better organization in the admin form
    fieldsets = (
        ('Client Information', {
            'fields': ('client', 'phone_number')
        }),
        ('Membership Details', {
            'fields': (
                'name',
                'membership_type',
                'price',
                'duration',
                'start_date',
                'end_date',
                'active',
            )
        }),
        ('Additional Information', {
            'fields': ('benefits', 'offer'),
        }),
    )

    # Read-only fields (if necessary)
    readonly_fields = ('start_date',)

    # Customize form field widgets (optional)
    def formfield_for_dbfield(self, db_field, **kwargs):
        from django.forms import Textarea

        if db_field.name == "offer":
            kwargs['widget'] = Textarea(attrs={'rows': 4, 'cols': 60})
        return super().formfield_for_dbfield(db_field, **kwargs)
