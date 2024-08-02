from django.test import TestCase
from django.contrib.auth.models import User
from .models import Customer, Product, Orders, Feedback

class CustomerModelTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', 
            password='testpassword',
            first_name='John',
            last_name='Doe'
        )
        self.customer = Customer.objects.create(
            user=self.user,
            address='123 Main St',
            mobile='1234567890'
        )

    def test_customer_str_method(self):
        self.assertEqual(str(self.customer), 'John')

    def test_customer_get_name(self):
        self.assertEqual(self.customer.get_name, 'John Doe')

    def test_customer_get_id(self):
        self.assertEqual(self.customer.get_id, self.user.id)

    
class ProductModelTests(TestCase):

    def setUp(self):
        self.product = Product.objects.create(
            name='Test Product',
            price=100,
            description='A test product description'
        )

    def test_product_str_method(self):
        self.assertEqual(str(self.product), 'Test Product')


class OrdersModelTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.customer = Customer.objects.create(user=self.user, address='123 Main St', mobile='1234567890')
        self.product = Product.objects.create(name='Test Product', price=100, description='A test product description')
        self.order = Orders.objects.create(
            customer=self.customer,
            product=self.product,
            email='test@example.com',
            address='123 Main St',
            mobile='1234567890',
            status='Pending'
        )

    def test_order_default_status(self):
        self.assertEqual(self.order.status, 'Pending')

    def test_order_customer_relationship(self):
        self.assertEqual(self.order.customer.user.username, 'testuser')

    def test_order_product_relationship(self):
        self.assertEqual(self.order.product.name, 'Test Product')

   
class FeedbackModelTests(TestCase):

    def setUp(self):
        self.feedback = Feedback.objects.create(
            name='John Doe',
            feedback='Great service!',
        )

    def test_feedback_str_method(self):
        self.assertEqual(str(self.feedback), 'John Doe')

    def test_feedback_date_auto_now_add(self):
        self.assertIsNotNone(self.feedback.date) 