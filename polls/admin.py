from django.contrib import admin

from .models import Question, Choice

# Register your models here.


class ChoiceInline(admin.TabularInline):
    model = Choice
    """
    tells Django to provide space for 3 choices in the form
    """
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'question_text', 'pub_date',
                    'was_published_recently')
    """
    the order of fields in the fields list dictates the order which it appears
    in the edit/create form. 
    """
    # fields = ['pub_date', 'question_text']

    """
    fieldsets help organize your fields into more user friendly sections
    """
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    """
    inlines add the ability to add related objects within the same form
    """
    inlines = [ChoiceInline]

    """
    Adds the filter functionality
    """
    list_filter = ['pub_date']
    """
    Adds search functionality
    """
    search_fields = ['question_text']


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'question_id', 'choice_text', 'votes')

    def question_id(self, obj):
        return obj.question.id


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
