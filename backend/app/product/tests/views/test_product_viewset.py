"""
Module containing the tests for the Product ViewSet.
"""

from django.urls import reverse
from mixer.backend.django import mixer
from rest_framework import status

from core.mixins import BaseAPITestCase
from product.models import Product


class ProductViewSetTestCase(BaseAPITestCase):
    """
    Class to test the Product ViewSet.
    """

    def test_should_require_authentication(self):
        """
        Method to assert that the endpoint requires authentication (the user must be logged in).
        """
        url = reverse('products-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_should_create_product_instance(self):
        """
        Method to assert we can create a new product object through the API using a POST method.
        """
        self.login()

        test_name = 'Test Product'
        test_description = 'Test Product Description'
        test_price = 100.00

        data = {
            'user': self.user.id,
            'name': test_name,
            'description': test_description,
            'price': test_price,
        }

        url = reverse('products-list')
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 1)

    def test_should_list_product_instances(self):
        """
        Method to assert we can list all products objects through the API using a GET method.
        """
        self.login()

        url = reverse('products-list')
        response = self.client.get(url)

        # Creating two product instances
        self._create_product_with_mixer(user=self.user)
        self._create_product_with_mixer(user=self.user)

        response = self.client.get(url)

        # Asserting that the response is OK and that the count is now 2
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['count'], 2)

    def test_should_retrieve_product_instance(self):
        """
        Method to assert we can retrieve a product object through the API using a GET method.
        """
        self.login()

        products = self._create_product_with_mixer(user=self.user)
        url = reverse('products-detail', kwargs={'pk': products.id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['id'], str(products.id))

    def test_should_update_product_instance(self):
        """
        Method to assert we can update a product object through the API using a PATCH method.
        """
        self.login()

        test_description = 'First product description'
        product = self._create_product_with_mixer(user=self.user, description=test_description)
        url = reverse('products-detail', kwargs={'pk': product.id})

        self.assertEqual(product.description, test_description)

        test_description = 'Second product description'
        response = self.client.patch(url, {'description': test_description})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['description'], test_description)

    def test_should_delete_product_instance(self):
        """
        Method to assert we can delete a product object through the API using a DELETE method.
        """
        self.login()

        product = self._create_product_with_mixer(user=self.user)

        self.assertEqual(Product.objects.count(), 1)

        url = reverse('products-detail', kwargs={'pk': product.id})
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Product.objects.count(), 0)

    def test_viewset_should_filter_products_by_user(self):
        """
        Method to assert the viewset filter products by user,
        returning only the products of the logged user.
        """
        self.login()

        # Creating two product instances
        self._create_product_with_mixer(user=self.user)
        self._create_product_with_mixer(user=self.user)

        # Creating a new user
        new_user = self.create_user()

        # Creating two product instances for the new user
        self._create_product_with_mixer(user=new_user)
        self._create_product_with_mixer(user=new_user)

        url = reverse('products-list')
        response = self.client.get(url)

        # Asserting that the response is OK and that the count is 2
        # (only the products of the logged user)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['count'], 2)

    def test_viewset_should_return_all_products_for_superuser(self):
        """
        Method to assert the viewset returns all products for a superuser.
        """
        self.login()

        # Creating two product instances
        self._create_product_with_mixer(user=self.user)
        self._create_product_with_mixer(user=self.user)

        # Creating a new user
        new_user = self.create_user()

        # Creating two product instances for the new user
        self._create_product_with_mixer(user=new_user)
        self._create_product_with_mixer(user=new_user)

        # Making the logged user a superuser
        self.user.is_superuser = True
        self.user.save()

        url = reverse('products-list')
        response = self.client.get(url)

        # Asserting that the response is OK and that the count is 4
        # (all products in the database)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['count'], 4)

    def test_should_filter_products_by_price(self):
        """
        Method to assert the viewset filters products by price.
        """
        self.login()

        url = reverse('products-list')

        # Creating five product instances
        self._create_product_with_mixer(user=self.user, price=100.00)
        self._create_product_with_mixer(user=self.user, price=200.00)
        self._create_product_with_mixer(user=self.user, price=300.00)
        self._create_product_with_mixer(user=self.user, price=400.00)
        self._create_product_with_mixer(user=self.user, price=500.00)

        # Testing filtering by GREATER THAN OR EQUAL TO
        with self.subTest('Filtering by greater than or equal to'):
            filter = {'price__gte': 300.00, 'ordering': 'price'}
            response = self.client.get(url, filter)
            results = response.json()['results']

            # Asserting that the response is OK and that the count is 3
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(response.json()['count'], 3)
            self.assertEqual(results[0]['price'], '300.00')
            self.assertEqual(results[1]['price'], '400.00')
            self.assertEqual(results[2]['price'], '500.00')

        # Testing filtering by LESS THAN OR EQUAL TO
        with self.subTest('Filtering by less than or equal to'):
            filter = {'price__lte': '300.00', 'ordering': 'price'}
            response = self.client.get(url, filter)
            results = response.json()['results']

            # Asserting that the response is OK and that the count is 3
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(response.json()['count'], 3)
            self.assertEqual(results[0]['price'], '100.00')
            self.assertEqual(results[1]['price'], '200.00')
            self.assertEqual(results[2]['price'], '300.00')

        # Testing filtering by RANGE
        with self.subTest('Filtering by range'):
            filter = {
                'price__gt': '100.00',
                'price__lt': '500.00',
                'ordering': 'price'
            }
            response = self.client.get(url, filter)
            results = response.json()['results']

            # Asserting that the response is OK and that the count is 3
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(response.json()['count'], 3)
            self.assertEqual(results[0]['price'], '200.00')
            self.assertEqual(results[1]['price'], '300.00')
            self.assertEqual(results[2]['price'], '400.00')

    def test_should_search_products_by_name(self):
        """
        Method to assert the viewset searches products by name.
        """
        self.login()

        url = reverse('products-list')

        # Creating two product instances
        self._create_product_with_mixer(user=self.user, name='Apple')
        self._create_product_with_mixer(user=self.user, name='Banana')

        # Testing searching by name
        filter = {'name': 'apple'}
        response = self.client.get(url, filter)
        results = response.json()['results']

        # Asserting that the response is OK and that the count is 1
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['count'], 1)
        self.assertEqual(results[0]['name'], 'Apple')

    def _create_product_with_mixer(self, *args, **kwargs) -> Product:
        """
        Method to create a product instance using mixer.
        """
        product: Product = mixer.blend(Product, *args, **kwargs)  # type: ignore

        return product
