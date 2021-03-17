from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from .models import *
import logging
from django.utils.translation import gettext as _


# Create your views here.
def main_page_view(request):
    return render(request, 'index.html', context={})


def search_result(request):
    user_search = request.GET.get('user_search')
    books = Book.objects.filter(is_visible=True).filter(
        Q(name__icontains=user_search) | Q(author__icontains=user_search)
    )
    return render(request, "search_result.html", context={'books': books})


def book_page_view(request, pk):
    book = Book.objects.get(pk=pk)
    return render(request, "book_page.html", context={'book': book})


def book_page_update(request, pk):
    book = Book.objects.filter(pk=pk).update(is_visible=False)
    return render(request, "reserve_done.html", context={'book': book})
