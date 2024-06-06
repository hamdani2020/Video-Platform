python3.9 -m venv env
source env/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run your build commands (e.g., collectstatic for Django)
python3.9 manage.py collectstatic --noinput

# Deactivate the virtual environment
deactivate