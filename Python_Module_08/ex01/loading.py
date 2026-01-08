import matplotlib.pyplot as plt
import importlib as ib
import requests as rq
import pandas as pd
import numpy as np
import matplotlib
import sys


def compare_versions():
    # Show installed package versions
    print("\nDependency version comparison:")
    print(f"Pandas version: {pd.__version__}")
    print(f"Requests version: {rq.__version__}")
    print(f"Matplotlib version: {matplotlib.__version__}\n")


def detect_environment():
    # Detect pip or poetry environment
    python_path = sys.executable

    if ".venv" in python_path or "poetry" in python_path.lower():
        return "poetry"
    return "pip"


def check_dependencies() -> dict:
    # Check if required packages are installed
    print("Checking dependencies:")
    dependencies = ["pandas", "requests", "matplotlib"]
    results = {}

    for d in dependencies:
        try:
            module = ib.import_module(d)  # Try to import module
            version = getattr(module, "__version__", "unknown")

            # Print status for each package
            if d == "pandas":
                print(f"[OK] {d} ({version}) - Data manipulation ready")
            elif d == "requests":
                print(f"[OK] {d} ({version}) - Network access ready")
            elif d == "matplotlib":
                print(f"[OK] {d} ({version}) - Visualization ready")
            else:
                print(f"[OK] {d} ({version})")

            results[d] = True
        except ImportError:
            # handle missing packages
            env = detect_environment()

            if env == "pip":
                print(f"[Missing] {d} — install with "
                      "\"pip install -r requirements.txt\"")
            elif env == "poetry":
                print(f"[Missing] {d} — install with \"poetry add {d}\"")

            results[d] = False

    return results


def test_requests() -> None:
    # Test HTTP request
    print("Testing requests:")
    try:
        re = rq.get("https://catfact.ninja/fact")
        data = re.json()
        print("Fact:", data["fact"])
    except Exception as e:
        print("Erro ao buscar dados:", e)


def analyzing_data():
    # Create sample Matrix-like data
    print("\nAnalyzing Matrix data...")
    print("Processing 1000 data points...")
    values = np.sort(np.random.choice(np.arange(0, 1000, 10), size=100))
    df = pd.DataFrame({"Y": values})
    return df


def generate_visualization(data) -> None:
    # Generate and save a plot
    print("Generating visualization...\n")
    plt.plot(data)
    plt.title("Matrix Analysis")
    plt.xlabel("X", size=15, labelpad=-5)
    plt.ylabel("Y", size=15, rotation=0, labelpad=5)
    plt.savefig("matrix_analysis.png")
    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png\n")


if __name__ == "__main__":
    print("LOADING STATUS: Loading programs...\n")

    env = detect_environment()
    if env == "pip":
        print("Environment: pip — dependencies managed via requirements.txt")
    elif env == "poetry":
        print("Environment: poetry — dependencies managed via pyproject.toml")

    compare_versions()  # Show package versions

    if all(check_dependencies().values()):
        # Run analysis only if all deps exist
        generate_visualization(analyzing_data())

    test_requests()
