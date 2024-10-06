from django.contrib import admin
from .models import Student,MarkSheet,Professor
# Register your models here.
# Assuming Professor model is used to assign professors

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'roll_number', 'email', 'project_title', 'total_marks', 'submission_status')
    readonly_fields = ('professor_marks', 'examiner1_marks', 'examiner2_marks', 'examiner3_marks','total_marks','total_midsem_marks','total_endsem_marks','professor_marks','examiner1_marks','examiner2_marks','examiner3_marks','professor_endmarks','examiner1_endmarks','examiner2_endmarks','examiner3_endmarks','submission_status')
    
    # Custom template for 'view more' feature
    change_form_template = 'student_change_form.html'

    def get_fields(self, request, obj=None):
        # Default fields to show
        fields = ['name', 'roll_number', 'email', 'project_title', 'presentation_date','presentation_from_time','presentation_to_time','professor','examiner1','examiner2','examiner3' ]
        if obj and request.GET.get('show_details', 'false') == 'true':
            # Add more fields when 'view more' is clicked
            fields += ['professor_marks', 'examiner1_marks', 'examiner2_marks', 'examiner3_marks','total_marks','total_midsem_marks','total_endsem_marks','professor_marks','examiner1_marks','examiner2_marks','examiner3_marks','professor_endmarks','examiner1_endmarks','examiner2_endmarks','examiner3_endmarks','submission_status']
        return fields

admin.site.register(Student, StudentAdmin)
admin.site.register(Professor)
admin.site.register(MarkSheet)