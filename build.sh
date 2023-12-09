# Install dependencies
pip install -r requirements.txt

mkdir -p staticfiles_build/static

python3.9 manage.py collectstatic

# Make migrations
python3.9 manage.py makemigrations
python3.9 manage.py migrate

# Get the superuser username from the environment variable
superuser_username="$DJANGO_SUPERUSER_USERNAME"

# Check if superuser with the specified username already exists
if python3.9 manage.py shell -c "from django.contrib.auth.models import User; print(User.objects.filter(username='$superuser_username').exists())" 2>/dev/null | grep -q "False"; then
    python3.9 manage.py createsuperuser --noinput --username="$superuser_username"
    echo "Superuser created"
else
    echo "Superuser with specified username already exists"
fi
