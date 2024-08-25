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
                'pk':product.id,
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
class ManageProduct(View):

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
@method_decorator(csrf_exempt, name='dispatch')
class Edit(View):
    def setup(self, request, *args, **kwargs):
        self.product = Product.objects.get(id=kwargs['pk'])
        return super().setup(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        if self.product:
            self.product.delete()
            return JsonResponse({'message': 'Product deleted successfully'}, status=204)
        return JsonResponse({'error': 'Product not found'}, status=404)

    def put(self, request, *args, **kwargs):
        if not self.product:
            return JsonResponse({'error': 'Product not found'}, status=404)

        cd = json.loads(request.body)
        self.product.name = cd.get('name', self.product.name)
        self.product.description = cd.get('description', self.product.description)
        self.product.price = int(cd.get('price', self.product.price))
        self.product.stock = int(cd.get('stock', self.product.stock))
        self.product.category_id = 1 if cd.get("category") == 'm' else 2
        self.product.save()
        return JsonResponse({'message': 'Product updated successfully'}, status=200)





