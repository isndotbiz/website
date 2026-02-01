#!/usr/bin/env python3
"""
Pre-flight checks for Premium Asset Generation
Verifies all requirements before running the asset generation pipeline
"""

import os
import sys
import subprocess
from pathlib import Path

def check_python_version():
    """Check Python version"""
    print("Checking Python version...", end=" ")
    version = sys.version_info
    if version.major >= 3 and version.minor >= 8:
        print(f"✓ Python {version.major}.{version.minor}.{version.micro}")
        return True
    else:
        print(f"✗ Python {version.major}.{version.minor}.{version.micro}")
        print("  ERROR: Python 3.8+ required")
        return False


def check_fal_api_key():
    """Check if FAL API key is set"""
    print("Checking FAL API key...", end=" ")
    key = os.getenv('FAL_API_KEY')
    if key:
        print(f"✓ Set ({len(key)} characters)")
        return True
    else:
        print("✗ Not set")
        print("\n  ERROR: FAL_API_KEY environment variable not set")
        print("  Please retrieve your key from 1Password: 'FAL API Key'")
        print("  Then run: export FAL_API_KEY='your-key-here'")
        return False


def check_aws_credentials():
    """Check AWS credentials"""
    print("Checking AWS credentials...", end=" ")
    try:
        result = subprocess.run(
            ['aws', 'sts', 'get-caller-identity'],
            capture_output=True,
            text=True,
            timeout=10
        )
        if result.returncode == 0:
            print("✓ Configured")
            return True
        else:
            print("⚠ Not configured (S3 upload will be skipped)")
            print("  Run 'aws configure' to enable S3 upload")
            return False
    except FileNotFoundError:
        print("⚠ AWS CLI not installed (S3 upload will be skipped)")
        return False
    except Exception as e:
        print(f"⚠ Error checking AWS: {e}")
        return False


def check_python_packages():
    """Check required Python packages"""
    print("\nChecking Python packages:")

    packages = {
        'requests': 'requests',
        'PIL': 'Pillow',
        'boto3': 'boto3'
    }

    all_installed = True

    for module_name, package_name in packages.items():
        print(f"  {package_name}...", end=" ")
        try:
            __import__(module_name)
            print("✓ Installed")
        except ImportError:
            print("✗ Not installed")
            all_installed = False

    if not all_installed:
        print("\n  To install missing packages:")
        print("  pip install -r requirements_assets.txt")

    return all_installed


def check_output_directory():
    """Check if output directory exists or can be created"""
    print("\nChecking output directory...", end=" ")
    output_dir = Path("/mnt/d/workspace/ISNBIZ_Files/assets/premium")

    try:
        output_dir.mkdir(parents=True, exist_ok=True)
        print(f"✓ {output_dir}")
        return True
    except Exception as e:
        print(f"✗ Cannot create directory: {e}")
        return False


def check_disk_space():
    """Check available disk space"""
    print("Checking disk space...", end=" ")
    try:
        import shutil
        total, used, free = shutil.disk_usage("/mnt/d/workspace/ISNBIZ_Files")
        free_gb = free // (2**30)

        if free_gb >= 1:
            print(f"✓ {free_gb} GB available")
            return True
        else:
            print(f"⚠ Only {free_gb} GB available (1GB+ recommended)")
            return False
    except Exception as e:
        print(f"⚠ Cannot check disk space: {e}")
        return True  # Don't fail on this


def check_internet_connection():
    """Check internet connectivity"""
    print("Checking internet connection...", end=" ")
    try:
        import requests
        response = requests.get('https://fal.run', timeout=5)
        print("✓ Connected")
        return True
    except:
        print("✗ Cannot reach fal.ai")
        print("  ERROR: Internet connection required")
        return False


def main():
    """Run all checks"""
    print("=" * 80)
    print("PREMIUM ASSET GENERATION - PRE-FLIGHT CHECKS")
    print("=" * 80)
    print()

    checks = [
        ("Python Version", check_python_version),
        ("FAL API Key", check_fal_api_key),
        ("AWS Credentials", check_aws_credentials),
        ("Output Directory", check_output_directory),
        ("Disk Space", check_disk_space),
        ("Internet Connection", check_internet_connection),
    ]

    results = {}

    # Run basic checks first
    for name, check_func in checks[:2]:
        results[name] = check_func()

    # Check packages
    results["Python Packages"] = check_python_packages()

    # Run remaining checks
    for name, check_func in checks[2:]:
        results[name] = check_func()

    # Summary
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)

    critical_checks = ["Python Version", "FAL API Key", "Python Packages",
                      "Output Directory", "Internet Connection"]
    optional_checks = ["AWS Credentials", "Disk Space"]

    critical_passed = all(results.get(check, False) for check in critical_checks)
    optional_passed = all(results.get(check, False) for check in optional_checks)

    if critical_passed and optional_passed:
        print("\n✓ ALL CHECKS PASSED")
        print("\nYou're ready to generate premium assets!")
        print("\nRun: ./generate_and_upload_premium_assets.sh")
        return 0
    elif critical_passed:
        print("\n✓ CRITICAL CHECKS PASSED")
        print("⚠ Some optional checks failed")
        print("\nYou can generate assets, but S3 upload may not work.")
        print("\nRun: ./generate_and_upload_premium_assets.sh")
        return 0
    else:
        print("\n✗ SOME CRITICAL CHECKS FAILED")
        print("\nPlease fix the issues above before proceeding.")
        print("\nFailed checks:")
        for check in critical_checks:
            if not results.get(check, False):
                print(f"  - {check}")
        return 1


if __name__ == '__main__':
    sys.exit(main())
