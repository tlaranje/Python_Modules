import sys
import os


if __name__ == "__main__":
    if "venv" in sys.prefix or "env" in sys.prefix:
        print("MATRIX STATUS: Welcome to the construct\n")

        env_path = os.path.dirname(os.path.dirname(sys.executable))
        env_name = os.path.basename(env_path)

        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment: {env_name}")
        print(f"Environment Path: {env_path}\n")

        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without "
              "affecting the global system.\n")

        python_version = f"python{sys.version_info.major}." \
                         f"{sys.version_info.minor}"
        site_packages_path = os.path.join(sys.prefix,
                                          "lib",
                                          python_version,
                                          "site-packages")
        print("Package installation path:")
        print(f"{site_packages_path}\n")
    else:
        print("MATRIX STATUS: You're still plugged in\n")

        print(f"Current Python: {sys.executable}")
        print("Virtual Environment: None detected\n")

        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.\n")

        print("To enter the construct, run:")
        print("python3 -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env")
        print("Scripts")
        print("activate # On Windows\n")

        print("Then run this program again.\n")
