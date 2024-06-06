python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run your build commands (e.g., collectstatic for Django)
python manage.py collectstatic --noinput

# Deactivate the virtual environment
deactivate