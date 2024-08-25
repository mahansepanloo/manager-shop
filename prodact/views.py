from django.shortcuts import render
from django.views import View
from .models import Product, Comment
from django.http import JsonResponse,HttpResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator





class Home(View):
    def get(self,reqeust):
        return render(reqeust,'home.html')


class Products(View):
    def get(self, request,order=None):
        products = Product.objects.all()
        if order:
            if order == "rate":
                products = sorted(products, key=lambda x: x.total_rate() or 0, reverse=True)
            else:
                products = products.order_by(f"-{order}")

        my_product_list = []

        for product in products:
            comments = Comment.objects.filter(product=product)


            ticket_dictionary = {
                "name": product.name,
                "price": product.price,
                "category": product.category.name,
                "seller": product.user.username,
                "stock": product.stock,
                "description": product.description,
                'total_rating': product.total_rate(),
                'comments': [(comment.buyer.username,comment.comment_text) for comment in comments]
            }

            my_product_list.append(ticket_dictionary)

        return JsonResponse(my_product_list, safe=False)



class Search(View):
    def get(self,request,searchs):
        products = Product.objects.all()
        products = products.filter(name__icontains=searchs)
        date = serializers.serialize('json',products)
        return JsonResponse(date, safe=False)

@method_decorator(csrf_exempt, name='dispatch')
class AddProduct(View):
    def post(self,request):
        cd = json.loads(request.body)
        if cd["category"] == 'm':
            i = 1
        else:
            i = 2

        prodact = Product.objects.create( user_id=1,name=cd['name'],
                               description=cd['description'],price=int(cd['price']),stock=int(cd['stock']),category_id=i)
        prodact.save()

        return HttpResponse('done')





