from django.contrib import admin

from tree.models import Game
class GameAdmin(admin.ModelAdmin):
    list_display = ("name",)


admin.site.register(Game, GameAdmin)