from django.contrib import admin

# Register your models here.
from site_setup import models


# @admin.register(models.MenuLink)
# class MenuLinkAdmin(admin.ModelAdmin):
#     list_display: tuple = (
#         "id",
#         "text",
#         "url_or_path",
#         "new_tab",
#     )
#     list_display_links: tuple = (
#         "id",
#         "text",
#         "url_or_path",
#     )
    
#     list_per_page: int = 20
#     list_max_show_all: int = 200

#     search_fields: tuple = (
#         # "id",
#         "text",
#         "url_or_path",
#     )

#     list_editable: tuple = ("new_tab",)


class MenuLinkInline(admin.TabularInline):
    model = models.MenuLink
    extra = 1


@admin.register(models.SiteSetup)
class SiteSetupAdmin(admin.ModelAdmin):
    list_display: tuple = (
        "title",
        "description",
        # "show_header",
        # "show_description",
        # "show_pagination",
        # "show_footer",
    )
    inlines: tuple = MenuLinkInline,
    
    def has_add_permission(self, request):
        return not models.SiteSetup.objects.exists()
    
    