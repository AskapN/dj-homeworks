from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scope, Tag

class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        check = 0
        for form in self.forms:
            if form.cleaned_data.get('DELETE', False):
                continue
            if form.cleaned_data.get('is_main', False):
                check += 1

            if check > 1:
                raise ValidationError('Основным может быть только один раздел')
            elif check == 0:
                raise ValidationError('Укажите основной раздел')
        return super().clean()


class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
