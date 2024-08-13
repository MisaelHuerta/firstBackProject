from django.test import TestCase
from config.wsgi import *
from core.erp.models import Type
# Create your tests here.

#Create

# t = Type()
# t.name = 'CTO'
# t.save()

#Read

query = Type.objects.all()
print(query)
print(Type.objects.all())

# #Update

# try:
#     t = Type.objects.get(id=2)
#     t.name = "CCO"
#     t.save()
# except Exception as e:
#     print(e)

#Delete

# try:
#     t = Type.objects.get(id=3)
#     t.delete()
# except Exception as e:
#     print(e)

#Read

query = Type.objects.filter(name__icontains="t").query
print(query)

for i in Type.objects.filter(name__contains="C"):
    print(i.name)
