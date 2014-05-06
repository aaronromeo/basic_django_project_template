# from factory import LazyAttribute
# from factory.django import DjangoModelFactory
#
# from .. import models
#
#
# class SampleFactory(DjangoModelFactory):
#     FACTORY_FOR = models.SampleModel
#
#     first_name = 'John'
#     last_name = 'Doe'
#     username = LazyAttribute(lambda a: '{0}.{1}'.format(a.first_name, a.last_name).lower())
#     email = LazyAttribute(lambda a: '{0}.{1}@example.com'.format(a.first_name, a.last_name).lower())
#
