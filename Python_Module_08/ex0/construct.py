import sys
import os


# This program checks whether it is running inside a Python virtual environment.

if __name__ == "__main__":
    try:
        # When inside a virtual environment, sys.prefix differs from
        # sys.base_prefix.
        if sys.prefix != sys.base_prefix:
            print("MATRIX STATUS: Welcome to the construct\n")

            # Show the full path of the Python executable currently in use
            print(f"Current Python: {sys.executable}")

            # Path to the active virtual environment
            virtual_env_path = sys.prefix

            # Extract the environment name from the path
            virtual_env_name = os.path.basename(virtual_env_path)

            print(f"Virtual Environment: {virtual_env_name}")
            print(f"Environment Path: {virtual_env_path}\n")

            print("SUCCESS: You're in an isolated environment!")
            print("Safe to install packages without "
                  "affecting the global system.\n")

            # Build the Python version string (e.g., python3.10)
            python_version = (f"python{sys.version_info.major}."
                              f"{sys.version_info.minor}")

            # Path to the site-packages directory inside the virtual environment
            virtual_site_packages = os.path.join(
                sys.prefix, "lib", python_version, "site-packages"
            )

            print("Package installation path (virtual environment):")
            print(f"{virtual_site_packages}\n")

            # Path to the global site-packages directory (outside the venv)
            global_site_packages = os.path.join(
                sys.base_prefix, "lib", python_version, "site-packages"
            )

            print("Global package installation path:")
            print(f"{global_site_packages}\n")

        else:
            # No virtual environment detected
            print("MATRIX STATUS: You're still plugged in\n")

            print(f"Current Python: {sys.executable}")
            print("Virtual Environment: None detected\n")

            print("WARNING: You're in the global environment!")
            print("Anything you install here affects the entire system.\n")

            # Instructions for creating and activating a virtual environment
            print("To enter the construct, run:")
            print("python3 -m venv matrix_env")
            print("source matrix_env/bin/activate  # On Unix/macOS")
            print("matrix_env\nScripts\nactivate   # On Windows\n")

            print("Then run this program again.\n")

    except Exception as error:
        # Catch unexpected errors and display them
        print("ERROR: Something went wrong while reading the environment.")
        print(f"Details: {error}")
