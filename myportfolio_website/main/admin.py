from django.contrib import admin
from .models import About, Count, Skill, Interest, Testimonial, Summary, Education, VoluntaryExperience, ProfessionalExperience, Service, Portfolio, PortfolioBanner

# Register your models here.

class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'birthday', 'city')
    search_fields = ('title', 'subtitle', 'city')

class CountAdmin(admin.ModelAdmin):
    list_display = ('title', 'value')
    search_fields = ('title',)

class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'value')
    search_fields = ('name',)

class InterestAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon')
    search_fields = ('name',)

class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'position')
    search_fields = ('name', 'position')

class SummaryAdmin(admin.ModelAdmin):
    list_display = ('location', 'phone', 'email')
    search_fields = ('location', 'email')

class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'institution', 'start_year', 'end_year')
    search_fields = ('degree', 'institution')
    list_filter = ('start_year', 'end_year')

class VoluntaryExperienceAdmin(admin.ModelAdmin):
    list_display = ('title', 'organization', 'start_date', 'end_date')
    search_fields = ('title', 'organization')
    list_filter = ('start_date', 'end_date')

class ProfessionalExperienceAdmin(admin.ModelAdmin):
    list_display = ('title', 'organization', 'start_date', 'end_date')
    search_fields = ('title', 'organization')
    list_filter = ('start_date', 'end_date')
       
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon', 'color')
    search_fields = ('title', 'description')

class PortfolioBannerInline(admin.TabularInline):
    model = PortfolioBanner
    extra = 1  # Number of empty forms to display

class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('title', 'service_type', 'category', 'project_date')
    search_fields = ('title', 'description', 'client')
    list_filter = ('category', 'service_type', 'project_date')
    inlines = [PortfolioBannerInline]

class PortfolioBannerAdmin(admin.ModelAdmin):
    list_display = ('portfolio', 'image')
    search_fields = ('portfolio__title',)
    

admin.site.register(About, AboutAdmin)
admin.site.register(Count, CountAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Interest, InterestAdmin)
admin.site.register(Testimonial, TestimonialAdmin)
admin.site.register(Summary, SummaryAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(VoluntaryExperience, VoluntaryExperienceAdmin)
admin.site.register(ProfessionalExperience, ProfessionalExperienceAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(PortfolioBanner, PortfolioBannerAdmin)