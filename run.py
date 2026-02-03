"""
GhostTrace – One Command Runner
Usage: python run.py
"""

import subprocess
import sys


def run_step(title: str, command: list[str]):
    print(f"\n🚀 {title}")
    print("-" * 50)
    result = subprocess.run(command, text=True)
    if result.returncode != 0:
        print(f"❌ Failed at step: {title}")
        sys.exit(1)


def main():
    print("🧠 GHOSTTRACE SYSTEM BOOTING")
    print("=" * 60)

    # STEP 1: Data ingestion (Role 1)
    run_step(
        "Running Data Ingestion (Role 1)",
        [sys.executable, "-m", "data_ingestion.run_metadata"]
    )

    # STEP 2: Risk Engine Tests (Role 3)
    run_step(
        "Running Risk Engine Tests (Role 3)",
        [sys.executable, "-m", "drift_analysis.test_queries"]
    )

    # STEP 3: Interactive RAG (Role 4)
    print("\n🧠 Starting Interactive RAG Engine (Role 4)")
    print("-" * 50)
    subprocess.run([sys.executable, "-m", "rag_engine.rag_pipeline"])


if __name__ == "__main__":
    main()
