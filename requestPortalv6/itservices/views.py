from django.shortcuts import render
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth import views as auth_views
from .models import *
import json
from pprint import pprint
import urllib2
import ast



def home_request(request):

    page_visit_count = []
    page_visit_url = []
    page_visit_head = []

    Page_visited_obj = Page_visited.objects.get(user=request.user)
    page_visit_count.append(Page_visited_obj.desktop_request)
    page_visit_url.append(Page_visited_obj.url_desktop)
    page_visit_head.append("desktop_request")

    page_visit_count.append(Page_visited_obj.it_assest_release)
    page_visit_url.append(Page_visited_obj.url_it_assest_release)
    page_visit_head.append("it_assest_release")


    page_visit_count.append(Page_visited_obj.usb_access)
    page_visit_url.append(Page_visited_obj.url_usb_access)
    page_visit_head.append("usb_access")

    page_visit_count.append(Page_visited_obj.software_requestion)
    page_visit_url.append(Page_visited_obj.url_software_requestion)
    page_visit_head.append("Software Requistion")

    page_visit_count.append(Page_visited_obj.dns)
    page_visit_url.append(Page_visited_obj.url_dns)
    page_visit_head.append("dns")


    page_visit_count.append(Page_visited_obj.link_proposal)
    page_visit_url.append(Page_visited_obj.url_link_proposal)
    page_visit_head.append("Link Proposal")

    page_visit_count.append(Page_visited_obj.network)
    page_visit_url.append(Page_visited_obj.url_network)
    page_visit_head.append("Network")


    page_visit_count.append(Page_visited_obj.admin_access)
    page_visit_url.append(Page_visited_obj.url_admin_access)
    page_visit_head.append("Admin Access")

    page_visit_dict = dict(zip(page_visit_url,page_visit_count))


    page_visit_1 = zip(page_visit_head,page_visit_url)

    import heapq
    from operator import itemgetter
    top_names = dict(heapq.nlargest(5, page_visit_dict.items(), key=itemgetter(1)))


    visit_top_url = top_names.keys()

    for url in visit_top_url:
        if url == "desktop_request/":
            top_names["desktop_request/"] = "desktop request"
        elif url == "asset_release/":
            top_names["asset_release/"] = "Asset Release"
        elif url == "usb_access/":
            top_names["usb_access/"] = "Usb Access"
        elif url == "admin_access/":
            top_names["admin_access/"] = "Admin Access"
        elif url == "dns/":
            top_names["dns/"] = "DNS"
        elif url == "software_req/":
            top_names["software_req/"] = "Software Requistion"
        elif url == "link_proposal/":
            top_names["link_proposal/"] = "Link Proposal"
        elif url == "network/":
            top_names["network/"] = "Network"
        else:
            pass


    return render(request, 'home/index.html', {'top_names':top_names})

def text_chat(request):

    return render(request, 'home/text.html', {})

def audio_chat(request):

    return render(request, 'home/audio.html', {})

def login(request):
    if request.method=="POST":
        user = request.POST.get('user')
        passwd = request.POST.get('passwd')

        if user=='demo'and passwd=='demo':



            return render(request, 'home/index.html', {})

        else:
            return HttpResponse("User name or passwd are incorrect" )
    else:
        return render(request, 'home/login.html', {})

    return HttpResponse("Success" )


def desktop_request(request):
    if request.method=="POST":

        city = request.POST.get('city')
        date = request.POST.get('datepicker')
        days = request.POST.get('days')
        l_type = request.POST.get('type')


        objDesktopRequest = Desktop.objects.create(user=str(request.user), location=city,date=date,days=days,laptop_type=l_type)
        objDesktopRequest.save()

        return render(request, 'home/desktop_request.submit.html', {})

    else:

        login_user = request.user

        page_visit_obj, created = Page_visited.objects.get_or_create(user=login_user)
        count =   page_visit_obj.desktop_request

        page_visit_obj.desktop_request =page_visit_obj.desktop_request+1
        page_visit_obj.save()

        return render(request, 'home/desktop_request.html', {})



def search(request):
    # with open('.\itservices\search.json') as data_file:
    #     data = json.load(data_file)
    #     list = []
    #     list.append(data['result'])
    #     dict_len  = len(data['result'])
    #     dict_len = dict_len + 1
    #     search_data = []
    #     search_data_url = []
    #     search_item_dict = {}
    #
    #     for i in range(1,dict_len):
    #         value = data['result']['search'+str(i)]['name']
    #         key = data['result']['search'+str(i)]['url']
    #         if type(value) == "list":
    #             l = value.split(',')
    #
    #         search_item_dict[key] = value


        # pprint(data1['result'])

        # d = dict(zip(search_data,search_data_url))
    # /   print "it is dict",d
        # d = {"request":"/request", "submit":"submit"}
    content = urllib2.urlopen("https://search-poc-domain-hepvzyiayiu5zqw6uhbw6qcfmq.us-east-1.cloudsearch.amazonaws.com/2013-01-01/search?q=Desktop&return=image_url").read()
    # print type(content)
    rid = []
    found =[]
    l_exp = []
    result = ast.literal_eval(content)
    new_len = len(result)+1
    len1 = len(result["hits"]["hit"])
    for i in range(0,len1):
        l_exp.append(result["hits"]["hit"][i]['fields']['image_url'])

    single_url = l_exp[0]
    new_dict = dict(zip(rid,found))

    search_text = request.POST.get('search')


    if search_text=='laptop' or search_text=='desktop':
        return render(request, 'home/search_link.html', {'content':content,'new_dict':new_dict,'l_exp':single_url})
    else:
        return render(request, 'home/dummy.html',{})

def link_search(request):


    return render(request, 'home/desktop_request.html', {})


def personalization(request):
    Page_visited_obj = Page_visited.objects.get(user==request.user)

    print Page_visited_obj.desktop_request

    return render(request, 'home/index.html', {})


def dummy(request):


    return render(request, 'home/dummy.html', {})
