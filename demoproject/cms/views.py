from django.shortcuts import render, get_object_or_404
from blog.models import Post
from .models import Page
from .forms import ContactForm

def home(request):

    about_page = Page.objects.filter(
        slug="about-us",
        is_published=True
    ).first()

    services_page = Page.objects.filter(
        slug="services",
        is_published=True
    ).first()

    latest_posts = Post.objects.filter(
        is_published=True
    ).order_by("-created_at")[:3]

    return render(
        request,
        "cms/home.html",
        {
            "about_page": about_page,
            "services_page": services_page,
            "latest_posts": latest_posts,
        },
    )


def page_detail(request, slug):

    page = get_object_or_404(
        Page,
        slug=slug,
        is_published=True
    )

    return render(
        request,
        "cms/page_detail.html",
        {
            "page": page,
        },
    )


def contact(request):

    if request.method == "POST":

        form = ContactForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("contact")

    else:

        form = ContactForm()

    return render(
        request,
        "cms/contact.html",
        {
            "form": form,
        }
    )