import pandas as pd
import os

def derive_features(df):
    # Calculate trip speed (miles per hour)
    # Assume trip_duration is in seconds
    df['trip_speed_mph'] = df['trip_distance'] / (df['trip_duration'] / 3600)
    df['trip_speed_mph'] = df['trip_speed_mph'].clip(upper=100)  # Limit unrealistic speeds

    # Calculate tip percentage
    df['tip_percentage'] = (df['tip_amount'] / df['total_amount'].replace(0, pd.NA)) * 100
    df['tip_percentage'] = df['tip_percentage'].fillna(0).clip(upper=100)

    # Mark peak hours
    df['is_peak_hour'] = df['pickup_hour'].isin([7, 8, 17, 18]).astype(int)

    # Categorize trip type based on duration (in minutes)
    df['trip_type'] = pd.cut(df['trip_duration'] / 60, bins=[0, 10, 30, float('inf')], labels=['short', 'medium', 'long'])

    return df

def clean_data(df):
    # Basic quality filters
    df = df.dropna(subset=['pickup_datetime', 'dropoff_datetime', 'trip_distance'])
    df = df[df['trip_distance'] > 0]
    df = df[df['total_amount'] > 0]
    # Calculate trip_duration if it doesn't exist
    if 'trip_duration' not in df.columns:
        df['pickup_datetime'] = pd.to_datetime(df['pickup_datetime'])
        df['dropoff_datetime'] = pd.to_datetime(df['dropoff_datetime'])
        df['trip_duration'] = (df['dropoff_datetime'] - df['pickup_datetime']).dt.total_seconds()
    df = df[df['trip_duration'] > 0]
    # Extract pickup_hour
    df['pickup_hour'] = df['pickup_datetime'].dt.hour
    return df

def main():
    input_file = 'data/nyc_taxi_raw.csv'
    output_file = 'data/nyc_taxi_enriched.csv'
    
    if not os.path.exists(input_file):
        print(f"Input file {input_file} not found.")
        return
    
    df = pd.read_csv(input_file)
    df = clean_data(df)
    df = derive_features(df)
    df.to_csv(output_file, index=False)
    print(f"Enriched data saved to {output_file}")

if __name__ == "__main__":
    main()