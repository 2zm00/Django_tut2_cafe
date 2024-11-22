from django.shortcuts import render
from .models import Menu, Option
# Create your views here.
def manager_index(request):
	return render(request, 'manager/index.html')

def menu_list(request):
	menus = Menu.objects.all()
	context = {
		"menus_to_page" : menus
	}
	return render(request, 'manager/menu_list.html', context=context)

def menu_add(request):
	return render(request, 'manager/menu_add.html')

def add_menu_data(request):
	menu_name_from_form = request.POST['menu_name']
	menu_price_from_form = request.POST['menu_price']
	Menu.objects.create(menu_name=menu_name_from_form, menu_price=menu_price_from_form)
	print(f"메뉴이름 : {menu_name_from_form}, 가격 : {menu_price_from_form} 이 추가되었습니다. ")

	return render(request, 'manager/menu_add.html')

def menu_detail(request,menu_id):
	# print("menu_id : ",menu_id)
	menu = Menu.objects.get(pk=menu_id)
	context = {
        "menu_to_page" : menu
    }
	return render(request, 'manager/menu_detail.html', context)

def add_option(request, menu_id):
    menu = Menu.objects.get(pk=menu_id)
    context = {"menu":menu}
    return render(request, 'manager/add_option.html', context)


def add_option_data(request):
	menu_id_from_form = request.POST['menu_id']
	option_name_from_form = request.POST['option_name']
	option_price_from_form = request.POST['option_price']
	menu = Menu.objects.get(pk=menu_id_from_form)
	Option.objects.create(menu=menu, option_name=option_name_from_form, option_price=option_price_from_form)
	context = {"menu_id":menu.id}
	return render(request, 'manager/add_option.html',context)