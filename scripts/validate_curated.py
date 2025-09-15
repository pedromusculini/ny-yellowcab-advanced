import pandas as pd
import os

def validate_curated_data(df):
    errors = []
    
    # Check trip speed
    if 'trip_speed_mph' in df.columns:
        invalid_speed = df[df['trip_speed_mph'] > 100]
        if not invalid_speed.empty:
            errors.append(f"Unrealistic speeds found: {len(invalid_speed)} records")
    
    # Check tip percentage
    if 'tip_percentage' in df.columns:
        invalid_tip = df[(df['tip_percentage'] < 0) | (df['tip_percentage'] > 100)]
        if not invalid_tip.empty:
            errors.append(f"Invalid tip percentages: {len(invalid_tip)} records")
    
    # Check trip type
    if 'trip_type' in df.columns:
        invalid_type = df[~df['trip_type'].isin(['short', 'medium', 'long'])]
        if not invalid_type.empty:
            errors.append(f"Invalid trip types: {len(invalid_type)} records")
    
    # Check peak hour indicator
    if 'is_peak_hour' in df.columns:
        invalid_peak = df[~df['is_peak_hour'].isin([0, 1])]
        if not invalid_peak.empty:
            errors.append(f"Invalid peak hour indicators: {len(invalid_peak)} records")
    
    return errors

def main():
    file_path = 'data/nyc_taxi_enriched.csv'
    
    if not os.path.exists(file_path):
        print(f"File {file_path} not found.")
        return
    
    df = pd.read_csv(file_path)
    errors = validate_curated_data(df)
    
    if errors:
        print("Validation errors found:")
        for error in errors:
            print(f"- {error}")
    else:
        print("Data validated successfully.")

if __name__ == "__main__":
    main()