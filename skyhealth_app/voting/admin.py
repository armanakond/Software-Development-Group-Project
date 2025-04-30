from django.contrib import admin
from .models import SurveySubmission, SurveyAnswer
 

# Register your models here.

@admin.register(SurveySubmission)
class SurveySubmissionAdmin(admin.ModelAdmin):
    list_display    = ('user', 'created_at')
    date_hierarchy  = 'created_at'
    search_fields   = ('user__username',)

@admin.register(SurveyAnswer)
class SurveyAnswerAdmin(admin.ModelAdmin):
    list_display   = ('submission', 'question_number', 'choice')
    list_filter    = ('question_number', 'choice')
    search_fields  = ('submission__user__username',)