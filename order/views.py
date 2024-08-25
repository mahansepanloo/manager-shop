from django.http import JsonResponse,HttpResponse
from django.views import View
from .models import Order

class Orders(View):
    def get(self,request):
        orders = Order.objects.all()
        # if order:
        #     if order == "totalprice":
        #         products = sorted(orders, key=lambda x: x.total_rate() or 0, reverse=True)
        #     else:
        #         products = orders.order_by(f"-{order}")
        my_product_list = []
        for product in orders:
                ticket_dictionary = {
                    "name": product.user.username,
                    "price": product.total_price(),
                    'itemorder': [product.all_product()]
                    }
                my_product_list.append(ticket_dictionary)
        data = sum([i.total_price() for i in orders])

        return JsonResponse((my_product_list,data), safe=False)




class Name_order(View):
    def get(self,requset,name):
        orders = Order.objects.filter(user__username=name)
        if orders.exists():
            my_product_list = []
            for product in orders:
                ticket_dictionary = {
                    "name": product.user.username,
                    "price": product.total_price(),
                    'itemorder': [product.all_product()],
                }
                my_product_list.append(ticket_dictionary)
            total_order = {'totalsum':sum([i.total_price() for i in orders])}
            my_product_list.append(total_order)

            return JsonResponse(my_product_list, safe=False)
        return HttpResponse('not found')

