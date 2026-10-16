set -e

# Install dependencies. The build image's python3 is 3.9 (too old for Django 5.2) and its
# uv-managed python3.12 refuses pip installs, so build in a venv.
python3.12 -m venv /tmp/build-venv
. /tmp/build-venv/bin/activate
pip install -r requirements.txt

mkdir -p staticfiles_build/static

python manage.py collectstatic

# Make migrations
python manage.py makemigrations
python manage.py migrate

# Get the superuser username from the environment variable
superuser_username="$DJANGO_SUPERUSER_USERNAME"

# Check if superuser with the specified username already exists
if python manage.py shell -c "from django.contrib.auth.models import User; print(User.objects.filter(username='$superuser_username').exists())" 2>/dev/null | grep -q "False"; then
    python manage.py createsuperuser --noinput --username="$superuser_username"
    echo "Superuser created"
else
    echo "Superuser with specified username already exists"
fi
