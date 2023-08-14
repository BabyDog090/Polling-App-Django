from django.contrib import admin
from .models import Poll, Choice, Vote


class ChoiceInline(admin.TabularInline):  # or admin.StackedInline for a different layout
    search_fields = ["text", "owner__username"]
    list_filter = ["active", 'created_at', 'pub_date']
    date_hierarchy = "pub_date"
    inlines = [ChoiceInline]


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ["choice_text", "poll", 'created_at', 'updated_at']
    search_fields = ["choice_text", "poll__text"]
    autocomplete_fields = ["poll"]


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ["choice", "poll", "user", 'created_at']
    search_fields = ["choice__choice_text", "poll__text", "user__username"]
    autocomplete_fields = ["choice", "poll", "user"]
