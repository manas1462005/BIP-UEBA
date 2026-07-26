"""Local development helper script for running backend and verifying setup."""
import sys
import subprocess

def run_backend():
    print("Starting FastAPI backend server via uvicorn...")
    subprocess.run([sys.executable, "-m", "uvicorn", "app.main:app", "--reload", "--port", "8000"], cwd="backend")

if __name__ == "__main__":
    run_backend()
