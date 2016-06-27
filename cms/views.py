from django.shortcuts import render
from cms.models import CmsPage
from champagn.enums import CmsPageType
# Create your views here.


def contactus(request):
    contacts = CmsPage.objects.filter(page_type=CmsPageType.CONTACT_US).first()
    context = {'contacts': contacts}
    return render(request, 'cms/contactus.html', context)


def aboutus(request):
    about = CmsPage.objects.filter(page_type=CmsPageType.ABOUT_US).first()
    context = {'about': about}
    return render(request, 'cms/aboutus.html', context)


def privacy(request):
    privacy = CmsPage.objects.filter(page_type=CmsPageType.PRIVACY).first()
    context = {'privacy': privacy}
    return render(request, 'cms/privacy.html', context)


def mediacontact(request):
    mediacontact = CmsPage.objects.filter(page_type=CmsPageType.MEDIA_CONTACT).first()
    context = {'mediacontact': mediacontact}
    return render(request, 'cms/mediacontact.html', context)


def termsofuse(request):
    termsofuse = CmsPage.objects.filter(page_type=CmsPageType.TERMS_OF_USE).first()
    context = {'termsofuse': termsofuse}
    return render(request, 'cms/termsofuse.html', context)


def investers(request):
    investers = CmsPage.objects.filter(page_type=CmsPageType.INVESTERS).first()
    context = {'investers': investers}
    return render(request, 'cms/investers.html', context)


def appdevelopers(request):
    appdevelopers = CmsPage.objects.filter(page_type=CmsPageType.APP_DEVELOPER).first()
    context = {'appdevelopers': appdevelopers}
    return render(request, 'cms/appdevelopers.html', context)
