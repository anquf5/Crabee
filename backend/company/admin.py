from django.contrib import admin
from .models import Company, CompanyReview
# Register your models here.

class reviewsInline(admin.TabularInline):
    model = CompanyReview
    fk_name = "company"

class company(admin.ModelAdmin):
    list_display = ['name', 'link']
    inlines = [reviewsInline]

class companyReview(admin.ModelAdmin):
    list_display = ['company', 'review_title', 'reviewer', 'pub_date']

admin.site.register(Company, company)
admin.site.register(CompanyReview, companyReview)
