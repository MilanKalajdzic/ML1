"""
Generate sample data for our first ML project
"""
import pandas as pd
import numpy as np
from pathlib import Path

def generate_housing_data(n_samples=1000):
    """Generate synthetic housing price data"""
    np.random.seed(42)
    
    # Generate features
    size = np.random.normal(1500, 500, n_samples)
    size = np.clip(size, 500, 5000)  # Realistic range
    
    bedrooms = np.random.poisson(2.5, n_samples) + 1
    bedrooms = np.clip(bedrooms, 1, 6)
    
    age = np.random.exponential(10, n_samples)
    age = np.clip(age, 0, 100)
    
    # Generate price based on features with some noise
    price = (
        size * 150 +  # $150 per sqft
        bedrooms * 5000 +  # $5000 per bedroom
        (50 - age) * 1000 +  # Newer houses worth more
        np.random.normal(0, 20000, n_samples)  # Random noise
    )
    price = np.clip(price, 50000, 1000000)  # Realistic range
    
    # Create DataFrame
    data = pd.DataFrame({
        'size_sqft': size.astype(int),
        'bedrooms': bedrooms.astype(int),
        'age_years': age.round(1),
        'price': price.astype(int)
    })
    
    return data

def main():
    """Generate and save sample data"""
    # Create data directory if it doesn't exist
    data_dir = Path('data/raw')
    data_dir.mkdir(parents=True, exist_ok=True)
    
    # Generate data
    housing_data = generate_housing_data(1000)
    
    # Save to CSV
    output_path = data_dir / 'housing_data.csv'
    housing_data.to_csv(output_path, index=False)
    
    print(f"Generated {len(housing_data)} samples")
    print(f"Saved to: {output_path}")
    print("\nData preview:")
    print(housing_data.head())
    print("\nData info:")
    print(housing_data.describe())

if __name__ == "__main__":
    main()