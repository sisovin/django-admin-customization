import os
import subprocess

def run_migrations():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
    try:
        result = subprocess.run(['python', 'manage.py', 'migrate'], check=True, capture_output=True, text=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error during migration: {e.stderr}")

if __name__ == "__main__":
    run_migrations()
