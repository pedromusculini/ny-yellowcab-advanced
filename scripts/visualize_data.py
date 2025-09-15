import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def create_visualizations():
    # Load enriched data
    file_path = 'data/nyc_taxi_enriched.csv'

    if not os.path.exists(file_path):
        print(f"File {file_path} not found. Please run data enrichment first.")
        return

    df = pd.read_csv(file_path)

    # Set up the plotting style
    plt.style.use('default')
    sns.set_palette("husl")

    # Create a directory for plots if it doesn't exist
    plots_dir = 'plots'
    os.makedirs(plots_dir, exist_ok=True)

    # Create subplots for multiple visualizations
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    fig.suptitle('NYC Taxi Data - New Features Analysis', fontsize=16, fontweight='bold')

    # 1. Trip Speed Distribution
    axes[0, 0].hist(df['trip_speed_mph'], bins=30, alpha=0.7, color='skyblue', edgecolor='black')
    axes[0, 0].set_title('Trip Speed Distribution (mph)', fontweight='bold')
    axes[0, 0].set_xlabel('Speed (mph)')
    axes[0, 0].set_ylabel('Frequency')
    axes[0, 0].axvline(df['trip_speed_mph'].mean(), color='red', linestyle='--', label=f'Mean: {df["trip_speed_mph"].mean():.1f} mph')
    axes[0, 0].legend()

    # 2. Tip Percentage Distribution
    axes[0, 1].hist(df['tip_percentage'], bins=20, alpha=0.7, color='lightgreen', edgecolor='black')
    axes[0, 1].set_title('Tip Percentage Distribution', fontweight='bold')
    axes[0, 1].set_xlabel('Tip Percentage (%)')
    axes[0, 1].set_ylabel('Frequency')
    axes[0, 1].axvline(df['tip_percentage'].mean(), color='red', linestyle='--', label=f'Mean: {df["tip_percentage"].mean():.1f}%')
    axes[0, 1].legend()

    # 3. Trip Type Distribution
    trip_type_counts = df['trip_type'].value_counts()
    axes[1, 0].bar(trip_type_counts.index, trip_type_counts.values, alpha=0.7, color=['lightcoral', 'gold', 'lightblue'])
    axes[1, 0].set_title('Trip Type Distribution', fontweight='bold')
    axes[1, 0].set_xlabel('Trip Type')
    axes[1, 0].set_ylabel('Count')

    # Add value labels on bars
    for i, v in enumerate(trip_type_counts.values):
        axes[1, 0].text(i, v + 0.5, str(v), ha='center', fontweight='bold')

    # 4. Peak Hour Analysis
    peak_hour_counts = df['is_peak_hour'].value_counts().sort_index()
    peak_hour_labels = ['Off-Peak', 'Peak Hour']
    axes[1, 1].pie(peak_hour_counts.values, labels=peak_hour_labels, autopct='%1.1f%%',
                   colors=['lightgray', 'orange'], startangle=90)
    axes[1, 1].set_title('Peak Hour Distribution', fontweight='bold')

    plt.tight_layout()
    plt.savefig(f'{plots_dir}/nyc_taxi_features_overview.png', dpi=300, bbox_inches='tight')
    plt.show()

    # Additional detailed plots
    create_detailed_plots(df, plots_dir)

    print(f"Visualizations saved to {plots_dir}/")

def create_detailed_plots(df, plots_dir):
    # Speed vs Distance scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['trip_distance'], df['trip_speed_mph'], alpha=0.6, color='purple')
    plt.title('Trip Speed vs Distance', fontweight='bold')
    plt.xlabel('Trip Distance (miles)')
    plt.ylabel('Trip Speed (mph)')
    plt.grid(True, alpha=0.3)
    plt.savefig(f'{plots_dir}/speed_vs_distance.png', dpi=300, bbox_inches='tight')
    plt.close()

    # Tip percentage by trip type
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='trip_type', y='tip_percentage', data=df, palette='Set3')
    plt.title('Tip Percentage by Trip Type', fontweight='bold')
    plt.xlabel('Trip Type')
    plt.ylabel('Tip Percentage (%)')
    plt.savefig(f'{plots_dir}/tip_by_trip_type.png', dpi=300, bbox_inches='tight')
    plt.close()

    # Speed distribution by peak hour
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df, x='trip_speed_mph', hue='is_peak_hour', multiple='stack',
                palette=['lightblue', 'salmon'], alpha=0.7)
    plt.title('Speed Distribution by Peak Hour', fontweight='bold')
    plt.xlabel('Trip Speed (mph)')
    plt.ylabel('Frequency')
    plt.legend(['Off-Peak', 'Peak Hour'])
    plt.savefig(f'{plots_dir}/speed_by_peak_hour.png', dpi=300, bbox_inches='tight')
    plt.close()

    # Correlation heatmap of new features
    new_features = ['trip_distance', 'trip_duration', 'trip_speed_mph', 'tip_percentage', 'is_peak_hour']
    corr_matrix = df[new_features].corr()

    plt.figure(figsize=(8, 6))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0, fmt='.2f')
    plt.title('Correlation Matrix of New Features', fontweight='bold')
    plt.savefig(f'{plots_dir}/correlation_matrix.png', dpi=300, bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    create_visualizations()