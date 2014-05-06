# from mock import patch
# from django.contrib.auth.models import User
# from django.test import TestCase, Client
#
# from rebar.testing import flatten_to_dict
#
# from ..forms import SampleForm
# from ..models import SomeModel
# from factories import SomeModelFactory
#
#
# class TestSampleForm(TestCase):
#     def setUp(self):
#         self.data = flatten_to_dict(SampleForm())
#         client = Client(enforce_csrf_checks=True)
#         self.request = client.request()
#         self.data['username'] = 'foo',
#         self.data['email'] = 'foo@example.com'
#         self.data['password'] = '123456'
#
#     def test_basic_form_valid(self):
#         form = SampleForm(self.data)
#         self.assertTrue(form.is_valid())
