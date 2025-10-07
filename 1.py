# hello_ml.py - Your first ML script
import sys
import platform

def main():
    print("🐍 Welcome to Machine Learning!")
    print(f"Python version: {sys.version}")
    print(f"Platform: {platform.system()}")
    
    # Simple data analysis example
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"\nData: {numbers}")
    print(f"Sum: {sum(numbers)}")
    print(f"Average: {sum(numbers) / len(numbers)}")
    print(f"Max: {max(numbers)}")
    print(f"Min: {min(numbers)}")

if __name__ == "__main__":
    main()