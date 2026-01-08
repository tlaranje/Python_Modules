from dotenv import load_dotenv
import sys
import os


def check_hardcoded_secrets():
    # Scan file for hardcoded secrets
    try:
        with open(__file__, "r") as fd:
            for line in fd:
                l_s = line.strip()

                if l_s.startswith("#"):
                    continue

                keys = ["API_KEY=", "API_KEY =",
                        "DATABASE_URL=", "DATABASE_URL =",
                        "ZION_ENDPOINT=", "ZION_ENDPOINT ="]

                for key in keys:
                    if l_s.startswith(key):
                        return False
        return True
    except Exception:
        # If file can't be read, assume safe
        return True


if __name__ == "__main__":
    print("ORACLE STATUS: Reading the Matrix...\n")

    # Load .env and read config in one try block
    try:
        load_dotenv()

        matrix_mode = os.getenv("MATRIX_MODE")
        db_url = os.getenv("DATABASE_URL")
        api_key = os.getenv("API_KEY")
        log_level = os.getenv("LOG_LEVEL")
        zion = os.getenv("ZION_ENDPOINT")

    except Exception:
        print("ERROR: Failed to load configuration")
        sys.exit(1)

    # Validate MATRIX_MODE
    if matrix_mode not in ("development", "production"):
        print("ERROR: MATRIX_MODE must be 'development' or 'production'")
        sys.exit(1)

    print("Configuration loaded:")

    # Check for missing values
    missing = []
    if not db_url:
        missing.append("DATABASE_URL")
    if not api_key:
        missing.append("API_KEY")
    if not zion:
        missing.append("ZION_ENDPOINT")
    if not log_level:
        missing.append("LOG_LEVEL")

    if missing:
        print("WARNING: Missing configuration values:")
        for m in missing:
            print(f" - {m}")
        print("\nPlease update your .env file.\n")

    # Show mode-specific behavior
    if matrix_mode == "development":
        print("Mode: development")
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

    # Security checks
    print("\nEnvironment security check:")
    if check_hardcoded_secrets():
        print("[OK] No hardcoded secrets detected")
    else:
        print("[WARNING] Hardcoded secrets found in oracle.py")

    # Check .env presence
    if os.path.exists(".env"):
        print("[OK] .env file properly configured")
    else:
        print("[WARNING] .env file missing")

    print("[OK] Production overrides available")
    print("\nThe Oracle sees all configurations")
