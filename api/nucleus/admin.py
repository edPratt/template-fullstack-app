from django.contrib import admin, messages
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from social_django.models import UserSocialAuth


User = get_user_model()


class UserSocialAuthInline(admin.StackedInline):
    model = UserSocialAuth
    extra = 0


class SocialAuthParser:
    def __init__(self, user):
        self.user = user

    def get_social_data(self, key):
        social_auth = self.user.social_auth.first()
        if social_auth:
            return social_auth.extra_data.get(key)

    def get_rank_data(self):
        return self.get_social_data('rank_data')

    def get_rank_item(self, key):
        rank_data = self.get_rank_data()
        if rank_data:
            return rank_data.get(key)

    @property
    def rank_label(self):
        return self.get_rank_item('rank')

    @property
    def rank_int(self):
        return self.get_rank_item('rank_int')

    @property
    def rank_leaderboard(self):
        return self.get_rank_item('rank_leaderboard')


class CustomUserAdmin(UserAdmin):
    list_display = (
        'username',
        'email',
        'is_staff',
        'rank_label',
        'rank_int',
        'rank_leaderboard',
    )
    inlines = UserAdmin.inlines + [
        UserSocialAuthInline,
    ]
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('email', )}),
        ('Ranking info', {'fields': ('rank_label', 'rank_int', 'rank_leaderboard', )}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',
                                    'groups', 'user_permissions'),
                         'classes': ('collapse', )}),
    )
    readonly_fields = UserAdmin.readonly_fields = (
        'rank_label',
        'rank_int',
        'rank_leaderboard',
    )

    def rank_label(self, obj):
        social_auth_parser = SocialAuthParser(obj)
        return social_auth_parser.rank_label

    def rank_int(self, obj):
        social_auth_parser = SocialAuthParser(obj)
        return social_auth_parser.rank_int

    def rank_leaderboard(self, obj):
        social_auth_parser = SocialAuthParser(obj)
        return social_auth_parser.rank_leaderboard


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
