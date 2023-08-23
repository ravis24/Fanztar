from rest_framework.response import Response
import uuid

class Order:
	order_id = 0

	def __init__(self, components_data, required_components):
		self.components_data = components_data
		self.required_components = required_components
		self.orders = [];
		

	def create_order(self, order_request_data):

		components_code = order_request_data['components']
		is_valid_order = self.validate_order(components_code)

		if not is_valid_order:
			return Response("Your order is not Valid")
		
		response_data = self.calculate_price(components_code)
		self.orders.append(response_data);
		return Response(response_data)


	def validate_order(self,components_code):

		requested_component_hash = {}
		for component_code in components_code:
			
			try:
				component_type  = self.components_data[component_code]['name'].split()[1]
			except:
				return False
			if component_type in requested_component_hash:
				requested_component_hash[component_type] += 1
			else:
				requested_component_hash[component_type] = 1

		for component_type in self.required_components:
			if (component_type not in requested_component_hash or
				requested_component_hash[component_type] > 1):
				return False
		else:
			return True


	def calculate_price(self, components_code):

		total_price = 0
		parts = []
		self.order_id += 1
		for component_code in components_code:
			total_price += self.components_data[component_code]['price']
			full_components_name = self.components_data[component_code]['name']
			parts.append(full_components_name)
		total_price = "{:.2f}".format(total_price)
		return {
			'order_id':self.order_id,
			'total':total_price,
			"parts":parts
		}
