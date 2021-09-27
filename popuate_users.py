import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE','ProTwo.settings')
import django
django.setup()


from faker import Faker

fake = Faker()


from AppTwo.models import UserNames

for x in range(10):
    fake_name = fake.first_name()
    fake_lname = fake.last_name()
    fake_email = fake.ascii_free_email()
    u = UserNames.objects.get_or_create(fname = fake_name,lname = fake_lname,email = fake_email)[0]
    u.save()
        

if __name__ == '__main__':
    print('populating')
    print('done')