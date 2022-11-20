from django.contrib import admin


from DogShelter.web.models import Dog, NoticeBoard, About, Donation
# Register your models here.


class PetInlineAdmin(admin.StackedInline):
    model = Dog


@admin.register(Dog)
class Dog(admin.ModelAdmin):
    readonly_fields = ('id',)
    list_display = ["id", "name_eng",  "status", "story_bg"]
    list_filter = ["status", "story_eng", "story_bg"]


@admin.register(NoticeBoard)
class NoticeBoard(admin.ModelAdmin):
    readonly_fields = ('id',)
    list_display = ["location", "note_bg"]


@admin.register(About)
class About(admin.ModelAdmin):
    readonly_fields = ('id',)


@admin.register(Donation)
class Donation(admin.ModelAdmin):
    readonly_fields = ('id',)
    list_display = ["person_name_eng", "date"]
