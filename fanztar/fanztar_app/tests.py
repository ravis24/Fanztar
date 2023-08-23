import unittest
from rest_framework import status
from .order import Order
from .components_data import components_data, required_component
# Create your tests here.

class OrderTestCase(unittest.TestCase):

	def setUp(self):
		self.order_instance = Order(components_data, required_component)

	def test_valid_order(self):
		components_code = ['A', 'D', 'F', 'I', 'K']
		result = self.order_instance.validate_order(components_code)
		self.assertTrue(result)

	def test_duplicate_component(self):
		components_code = ['A', 'B', 'B','G','J']
		result = self.order_instance.validate_order(components_code)
		self.assertFalse(result)

	def test_missing_component(self):
		components_code = ['B', 'E', 'F','I']
		result = self.order_instance.validate_order(components_code)
		self.assertFalse(result)

	def test_complete_with_duplicate_component(self):
		components_code = ["B","D","F","I","K","B"]
		result = self.order_instance.validate_order(components_code)
		self.assertFalse(result)

	def test_different_component(self):
		components_code = ['B', 'E', 'F','I','Z']
		result = self.order_instance.validate_order(components_code)
		self.assertFalse(result)

	def test_valid_create_order(self):
		data = {"components": ['A', 'D', 'F', 'I', 'K']} 
		response = self.order_instance.create_order(data)
		self.assertEqual(response.data['total'], "142.30") 
		self.assertEqual(len(response.data['parts']), 5)

	def test_calculate_price(self):
		components_code = ['A', 'D', 'F', 'I', 'K']
		response = self.order_instance.calculate_price(components_code)
		self.assertEqual(response['order_id'], 1)
		self.assertEqual(response['total'], "142.30")
		self.assertEqual(len(response['parts']), 5)