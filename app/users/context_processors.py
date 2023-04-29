from django.conf import settings  # import the settings file


def debug(request):
    return {
        'IS_DEMONSTRATION_MODE': settings.IS_DEMONSTRATION_MODE
    }
