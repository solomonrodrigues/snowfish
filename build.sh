set -e

# Install dependencies (the build image's python3 is 3.9, too old for Django 5.2)
dnf install -y python3.12 python3.12-pip
python3.12 -m pip install -r requirements.txt

mkdir -p staticfiles_build/static

python3.12 manage.py collectstatic

# Make migrations
python3.12 manage.py makemigrations
python3.12 manage.py migrate

# Get the superuser username from the environment variable
superuser_username="$DJANGO_SUPERUSER_USERNAME"

# Check if superuser with the specified username already exists
if python3.12 manage.py shell -c "from django.contrib.auth.models import User; print(User.objects.filter(username='$superuser_username').exists())" 2>/dev/null | grep -q "False"; then
    python3.12 manage.py createsuperuser --noinput --username="$superuser_username"
    echo "Superuser created"
else
    echo "Superuser with specified username already exists"
fi
