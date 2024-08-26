from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Address
from django.views import View
from django.http import JsonResponse
from django.core import serializers




# from django.db.models import Prefetch
#
# class Member(View):
#     def get(self, request):
#         users = User.objects.prefetch_related(Prefetch('address_set')).all()
#
#         my_product_list = []
#         for user in users:
#             addresses = user.address_set.all()
#             serialized_addresses = serializers.serialize('json', addresses)
#             ticket_dictionary = {
#                 "name": user.username,
#                 "id": user.id,
#                 "address": serialized_addresses
#             }
#             my_product_list.append(ticket_dictionary)
#
#         return JsonResponse(my_product_list, safe=False)




class Memmber(View):
    def get(self,reqeust):
        user = User.objects.all()
        a = Address.objects.all()

        my_product_list = []
        for product in user:
            aa=a.filter(user_id=product.id)
            sa=serializers.serialize('json',aa)
            ticket_dictionary = {
                "name": product.username,
                "id": product.id,
                'address':[sa]
            }
            my_product_list.append(ticket_dictionary)

        return JsonResponse(my_product_list, safe=False)
