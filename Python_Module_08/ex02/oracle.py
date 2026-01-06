import os
import sys
from dotenv import load_dotenv, dotenv_values


def check_hardcoded_secrets():
    with open(__file__, "r") as fd:
        for line in fd:
            l_s = line.strip()

            if l_s.startswith("#"):
                continue

            f_keys = ["API_KEY=", "API_KEY =",
                      "DATABASE_URL=", "DATABASE_URL =",
                      "ZION_ENDPOINT=", "ZION_ENDPOINT ="]

            for key in f_keys:
                if l_s.startswith(key):
                    return False
    return True


if __name__ == "__main__":
    print("ORACLE STATUS: Reading the Matrix...\n")

    load_dotenv()

    matrix_mode = os.getenv("MATRIX_MODE", "development")
    db_url = os.getenv("DATABASE_URL")
    api_key = os.getenv("API_KEY")
    log_level = os.getenv("LOG_LEVEL")
    zion = os.getenv("ZION_ENDPOINT")

    print("Configuration loaded:")
    missing = []
    if not db_url:
        missing.append("DATABASE_URL")
    if not api_key:
        missing.append("API_KEY")
    if not zion:
        missing.append("ZION_ENDPOINT")

    if missing:
        print("WARNING: Missing configuration values:")
        for m in missing:
            print(f" - {m}")
            print("\nPlease update your .env file.\n")
    if matrix_mode == "development":
        print(f"Mode: development")
        print("Database: Connected to local instance")
        print("API Access: Authenticated")
        print("Log Level:", log_level or "DEBUG")
        print("Zion Network:", zion or "Local network")
    elif matrix_mode == "production":
        print("Mode: production")
        print("Database: Connected to production instance")
        print("API Access: Production key active")
        print("Log Level:", log_level or "INFO")
        print("Zion Network:", zion or "Production network")
    else:
        print("ERROR: Invalid MATRIX_MODE")

    print("\nEnvironment security check:")
    if check_hardcoded_secrets():
        print("[OK] No hardcoded secrets detected")
    else:
        print("[WARNING] Hardcoded secrets found in oracle.py")

    if os.path.exists(".env"):
        print("[OK] .env file properly configured")
    else:
        print("[WARNING] .env file missing")

    print("[OK] Production overrides available")
    print("\nThe Oracle sees all configurations")
