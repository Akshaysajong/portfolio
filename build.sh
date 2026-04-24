#!/usr/bin/env bash

pip install -r requirements.txt

python manage.py collectstatic --noinput
python manage.py migrate

# FORCE create/update admin user
echo "from django.contrib.auth import get_user_model;
User = get_user_model();
u, created = User.objects.get_or_create(username='admin');
u.set_password('admin123');
u.is_staff = True;
u.is_superuser = True;
u.save()" | python manage.py shell