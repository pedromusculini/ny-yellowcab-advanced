import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.path import Path
import numpy as np

def create_project_logo():
    """Create a professional logo for the NYC Taxi Data Analysis project"""

    # Create figure with specific size for logo
    fig, ax = plt.subplots(figsize=(4, 4), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    # Background circle
    background = patches.Circle((50, 50), 45, facecolor='#1f2937', edgecolor='#3b82f6', linewidth=3)
    ax.add_patch(background)

    # Taxi body (yellow rectangle)
    taxi_body = patches.Rectangle((25, 35), 50, 20, facecolor='#fbbf24', edgecolor='#d97706', linewidth=2)
    ax.add_patch(taxi_body)

    # Taxi roof (darker yellow)
    taxi_roof = patches.Rectangle((30, 45), 40, 10, facecolor='#f59e0b', edgecolor='#d97706', linewidth=2)
    ax.add_patch(taxi_roof)

    # Wheels
    wheel1 = patches.Circle((35, 30), 5, facecolor='#374151', edgecolor='#1f2937', linewidth=2)
    wheel2 = patches.Circle((65, 30), 5, facecolor='#374151', edgecolor='#1f2937', linewidth=2)
    ax.add_patch(wheel1)
    ax.add_patch(wheel2)

    # Wheel rims
    rim1 = patches.Circle((35, 30), 2, facecolor='#9ca3af', edgecolor='#6b7280', linewidth=1)
    rim2 = patches.Circle((65, 30), 2, facecolor='#9ca3af', edgecolor='#6b7280', linewidth=1)
    ax.add_patch(rim1)
    ax.add_patch(rim2)

    # Taxi light on top
    taxi_light = patches.Rectangle((45, 55), 10, 3, facecolor='#ef4444', edgecolor='#dc2626', linewidth=1)
    ax.add_patch(taxi_light)

    # Data visualization elements (representing analytics)
    # Bar chart in the background
    bar1 = patches.Rectangle((15, 15), 3, 15, facecolor='#3b82f6', alpha=0.8)
    bar2 = patches.Rectangle((20, 15), 3, 25, facecolor='#10b981', alpha=0.8)
    bar3 = patches.Rectangle((25, 15), 3, 20, facecolor='#f59e0b', alpha=0.8)
    bar4 = patches.Rectangle((30, 15), 3, 30, facecolor='#ef4444', alpha=0.8)
    ax.add_patch(bar1)
    ax.add_patch(bar2)
    ax.add_patch(bar3)
    ax.add_patch(bar4)

    # Speed lines (representing motion)
    for i in range(3):
        speed_line = patches.Rectangle((75 + i*3, 40 + i*2), 8, 1, facecolor='#6b7280', alpha=0.6)
        ax.add_patch(speed_line)

    # Project title text
    ax.text(50, 85, 'NYC TAXI', ha='center', va='center', fontsize=12, fontweight='bold', color='white')
    ax.text(50, 78, 'ANALYTICS', ha='center', va='center', fontsize=8, color='#e5e7eb')

    # Save the logo
    plt.savefig('nyc_taxi_logo.png', dpi=300, bbox_inches='tight', transparent=True)
    plt.savefig('nyc_taxi_logo.svg', format='svg', bbox_inches='tight', transparent=True)

    print("Logo files created:")
    print("- nyc_taxi_logo.png (main logo)")
    print("- nyc_taxi_logo.svg (vector logo)")

if __name__ == "__main__":
    create_project_logo()