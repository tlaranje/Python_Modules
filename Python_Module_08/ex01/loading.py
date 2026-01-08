import matplotlib.pyplot as plt
import importlib as ib
import requests as rq
import pandas as pd
import numpy as np
import sys

def compare_versions():
    print("\nDependency version comparison:")
    print(f"Environment detected: {detect_environment()}")
    print(f"Pandas version: {pd.__version__}")
    print(f"Requests version: {rq.__version__}")
    print(f"Matplotlib version: {plt.__version__}")

def detect_environment():
    python_path = sys.executable

    if ".venv" in python_path or "poetry" in python_path.lower():
        return "poetry"
    return "pip"


def check_dependencies():
    print("Checking dependencies:")
    dependencies = ["pandas", "requests", "matplotlib"]
    results = {}

    for d in dependencies:
        try:
            module = ib.import_module(d)
            version = getattr(module, "__version__", "unknown")

            if d == "pandas":
                print(f"[OK] {d} ({version}) - Data manipulation ready")
            elif d == "requests":
                print(f"[OK] {d} ({version}) - Network access ready")
            elif d == "matplotlib":
                print(f"[OK] {d} ({version}) - Visualization ready")
            else:
                print(f"[OK] {d} ({version})")

            compare_versions()
            results[d] = True
        except ImportError:
            if detect_environment() == "pip":
                print(f"[Missing] {d} — install with "
                      "\"pip install -r requirements.txt\"")
            else:
                print(f"[Missing] {d} — install with \"poetry add {d}\"")
            results[d] = False

    return results


def test_requests():
    try:
        re = rq.get("https://catfact.ninja/fact")
        data = re.json()
        print("Fact:", data["fact"])
    except Exception as e:
        print("Erro ao buscar dados:", e)


def analyzing_data():
    print("\nAnalyzing Matrix data...")
    print("Processing 1000 data points...")
    values = np.sort(np.random.choice(np.arange(0, 1000, 10), size=100))
    df = pd.DataFrame({"Y": values })
    return df


def generate_visualization(data):
    print("Generating visualization...\n")
    plt.plot(data)
    plt.title("Matrix Analysis")
    plt.xlabel("X", size=15, labelpad=-5)
    plt.ylabel("Y", size=15, rotation=0, labelpad=5)
    plt.savefig("matrix_analysis.png")
    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    print("LOADING STATUS: Loading programs...\n")
    deps = check_dependencies()
    if all(deps.values()):
        generate_visualization(analyzing_data())
    else:
        print("\nSome dependencies are missing. Install them and try again.")
