from django.contrib import admin

from work_cards.models import WorkCard


@admin.register(WorkCard)
class WorkCardAdmin(admin.ModelAdmin):
    list_display = ("id", "contract_type", "available_from", "hours_per_week", "abroad")
    list_filter = ("contract_type", "available_from", "hours_per_week", "minimal_education_level", "abroad", "branches")
    search_fields = ("user__username", "key_skills", "looking_for", "current_client")
