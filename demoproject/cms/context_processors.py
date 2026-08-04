from .models import Menu, SiteSetting

def global_data(request):
    return {
        "menus": Menu.objects.filter(
            is_active=True,
            parent=None,
            location="header"
        ).order_by("order"),

        "footer_menus": Menu.objects.filter(
            is_active=True,
            parent=None,
            location="footer"
        ).order_by("order"),

        "site": SiteSetting.objects.first(),
    }

# Create your global menu here.
