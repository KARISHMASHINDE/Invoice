from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import os




def make_pages(query, size, data, url):
    paginator = Paginator(query, size)
    if 'page' not in data:
        page = 1
    else:
        page = data.get('page')
    try:
        page_query = paginator.page(page)
    except PageNotAnInteger:
        page_query = paginator.page(1)
        url = url.replace("page=" + page, "")
        page = 1
    except EmptyPage:
        page_query = paginator.page(paginator.num_pages)
        url = url.replace("page=" + page, "")
        page = paginator.num_pages
    page = int(page)
    pages = {}
    if '?' in url:
        if not page + 1 > paginator.num_pages:
            if 'page' not in url:
                next_url = url + '&page=' + str(page + 1)
            else:
                next_url = url.replace('page=' + str(page), "page=" + str(page + 1))
            pages.update({'next': next_url})
        if not page == 1:
            if 'page' not in url:
                prev_url = url + '&page=' + str(page - 1)
            else:
                prev_url = url.replace('page=' + str(page), "page=" + str(page - 1))
            pages.update({'prev': prev_url})
    else:
        if not page + 1 > paginator.num_pages:
            if 'page' not in url:
                next_url = url + '?page=' + str(page + 1)
            else:
                next_url = url.replace('page=' + str(page), "page=" + str(page + 1))
            pages.update({'next': next_url})
        if not page == 1:
            if 'page' not in url:
                prev_url = url + '?page=' + str(page - 1)
            else:
                prev_url = url.replace('page=' + str(page), "page=" + str(page - 1))
            pages.update({'prev': prev_url})
    return page_query, pages

    
