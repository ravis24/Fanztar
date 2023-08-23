from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .order import Order
from .components_data import components_data, required_component

create_order = Order(components_data,required_component)

@api_view(['POST'])
def order_api(request):

	get_response = create_order.create_order(dict(request.data))

	return Response(get_response.data)


