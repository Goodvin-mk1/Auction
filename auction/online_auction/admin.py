from django.contrib import admin
from .models import Category, Lot, Event, Bet, FeedBack


@admin.action(description='Опубликовать')
def make_public(self, request, queryset):
    queryset.update(is_published=True)


@admin.action(description='Снять с публикации')
def make_unpublic(self, request, queryset):
    queryset.update(is_published=False)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    actions = (make_public, make_unpublic)
    list_display = ('id', 'name', 'parent', 'is_published')
    list_filter = ('is_published', 'parent')
    search_fields = ('name', 'id')
    search_help_text = 'name/id'
    list_display_links = ('id', 'name')


@admin.register(Lot)
class LotAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'article', 'category', 'owner', 'created_date')
    list_filter = ('category', 'created_date', 'owner')
    search_fields = ('name', 'id', 'article', 'owner', 'category')
    search_help_text = 'name/id/article/owner/category'
    list_display_links = ('id', 'name')


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'lot', 'start_date', 'end_date', 'is_started', 'is_closed')
    list_filter = ('buyout_price', 'is_started', 'is_closed')
    search_fields = ('id', 'name', 'lot')
    search_help_text = 'id/name/lot/'
    list_display_links = ('id', 'name')


@admin.register(Bet)
class BetAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'event', 'created_date', 'bet')
    list_filter = ('event', 'user', 'created_date')
    search_fields = ('id', 'user', 'event')
    search_help_text = 'id/user/event/'
    list_display_links = ('id', 'event', 'user')


@admin.register(FeedBack)
class FeedBackAdmin(admin.ModelAdmin):
    readonly_fields = ('email', 'message', 'created_date')
    list_display = ('id', 'email', 'created_date')
    list_filter = ('created_date', )
    search_fields = ('id', 'email')
    search_help_text = 'id/email'
    list_display_links = ('id', 'email')
