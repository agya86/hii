from django.contrib import admin
from .models import Question,Choice
# Register your models here.
#admin.site.register(Question)
#class QuestionAdmin(admin.ModelAdmin):
#    fields = ['pub_date', 'question_text']
#admin.TabularInline
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3
    
#admin.site.register(Choice,ChoiceInline)
class QuestionAdmin(admin.ModelAdmin):
    '''
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date','classes':['collapse']]}),
    ]
    '''
    fieldsets = [
        ('Question', {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'],'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

    list_display = ('question_text', 'pub_date')
    list_filter = ('question_text', 'pub_date')
admin.site.register(Question, QuestionAdmin)