from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

challenge_monthes = {"january": 'Do push ups',
                     'february':'learn spanish',
                     'march':'eat healty',
                     'april': 'go on a vacation',
                     'may': "Maybe do something",
                     "june": 'Do push ups',
                     'july':'learn spanish',
                     'august':'eat healty',
                     'september': 'go on a vacation',
                     'october': 'buhhah',
                     'november': 'frerfe',
                     'december': 'fewfwe'}

def index_main(request):
    """returns an html page <ul><li>...</li></ul>"""
    month_list = "<ul>"
    for k,v in challenge_monthes.items():
        month_item = k.capitalize()
        month_path = reverse("month_challenge", args=[k])
        list_item = f"<li><a href={month_path}>{month_item}</a></li>"
        month_list += list_item

    month_list += "</ul>"
    return HttpResponse(month_list)

def challenge_index_number(request, month: int):
    if 0 < month < 12:
        converted__month = list(challenge_monthes.keys())[month-1]
        reversed_month_url = reverse("month_challenge", args=[converted__month])
        return HttpResponseRedirect(reversed_month_url)
    else:
        return HttpResponseNotFound(f"{month} is not a month")

def challenge_index(request, month):

    try:
        resp_text = challenge_monthes[month]
        return HttpResponse(resp_text)
    except KeyError:
        return HttpResponseNotFound(f"{month} is not a month")