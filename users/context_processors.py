from django.conf import settings  # import the settings file


def debug(request):
    return {
        'ALLOW_DEMO_USER': settings.ALLOW_DEMO_USER
    }
