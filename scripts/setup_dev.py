#!/usr/bin/env python3
"""
Developer environment setup and database initialization script for Behavioral Intelligence Platform.
"""
import os
import sys
import subprocess


def run_cmd(command: str, cwd: str = "."):
    print(f"==> Running: {command} in {cwd}")
    res = subprocess.run(command, shell=True, cwd=cwd)
    if res.returncode != 0:
        print(f"❌ Command failed with return code {res.returncode}")
        sys.exit(res.returncode)


def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    backend_dir = os.path.join(base_dir, "backend")

    print("🚀 Starting Behavioral Intelligence Platform Dev Setup...")
    
    # Run Alembic Upgrade
    print("\n📦 Running Alembic database migrations...")
    run_cmd("alembic upgrade head", cwd=backend_dir)

    print("\n✅ Setup complete! Phase 1 Architecture Foundation is ready.")


if __name__ == "__main__":
    main()
