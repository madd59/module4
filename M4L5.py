"""
M4L5.py

This Python program analyzes global fire data using popular Python libraries for data analysis and visualization:
pandas, matplotlib, seaborn, and numpy.

Key Features:
-------------
1. Loads a CSV dataset with fire data by country, year, and land cover type.
2. Summarizes fire activity by country, year, and land cover category.
3. Creates visualizations:
   - Bar chart of top countries by burned area.
   - Heatmap of fire activity by land cover type for top countries.
   - A simulated global map showing fire intensity.
4. Prints summary statistics for reporting and saves charts as PNG files.
5. Handles errors for missing files and unexpected issues.

The purpose is to demonstrate real-world data analysis using Python with clear outputs and visual insights.
"""

# Importing necessary libraries for data manipulation, visualization, and numerical computations
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from matplotlib.patches import Rectangle
import warnings
# Suppress unnecessary warning messages for cleaner output
warnings.filterwarnings('ignore')

# --------------------------
# Function: Load and Process Fire Data
# --------------------------
# This function reads the fire data from a CSV file, displays basic dataset information
# such as number of rows, columns, years covered, and unique countries.
def load_and_process_fire_data(csv_file_path):
    print("Loading fire data...")
    
    df = pd.read_csv(csv_file_path)
    
    print(f"Dataset loaded successfully!")
    print(f"Shape: {df.shape}")
    print(f"Years covered: {df['year'].min()} - {df['year'].max()}")
    print(f"Countries: {df['country'].nunique()}")
    
    return df

# --------------------------
# Function: Create Country Fire Summary
# --------------------------
# This function aggregates burned area data by country for different land cover types.
# It calculates total burned area per country and sorts them in descending order.
def create_country_fire_summary(df):
    """
    Create summary statistics by country
    """
    fire_columns = ['forest', 'savannas', 'shrublands_grasslands', 'croplands', 'other']
    country_summary = df.groupby('country')[fire_columns].sum()
    country_summary['total_burned_area'] = country_summary.sum(axis=1)
    country_summary = country_summary.sort_values('total_burned_area', ascending=False)
    return country_summary

# --------------------------
# Function: Create Yearly Trend Analysis
# --------------------------
# This function groups the data by year to show the trend of burned areas over time
# for each land cover type and overall totals.
def create_yearly_trend_analysis(df):
    """
    Analyze fire trends over years
    """
    fire_columns = ['forest', 'savannas', 'shrublands_grasslands', 'croplands', 'other']
    
    yearly_summary = df.groupby('year')[fire_columns].sum()
    yearly_summary['total_burned_area'] = yearly_summary.sum(axis=1)
    
    return yearly_summary

# --------------------------
# Function: Create Land Cover Analysis
# --------------------------
# This function calculates the total burned area for each land cover type globally.
def create_land_cover_analysis(df):
    """
    Analyze fire distribution across different land cover types
    """
    fire_columns = ['forest', 'savannas', 'shrublands_grasslands', 'croplands', 'other']
    
    land_cover_totals = df[fire_columns].sum()
    
    return land_cover_totals

# --------------------------
# Function: Plot Top Countries by Burned Area
# --------------------------
# This function creates a bar chart showing the top countries with the highest burned area.
# It also annotates each bar with its value and saves the chart as a PNG file.
def plot_top_countries_burned_area(country_summary, top_n=20):
    """
    Plot top countries by total burned area
    """
    plt.figure(figsize=(15, 8))
    
    top_countries = country_summary.head(top_n)
    
    bars = plt.bar(range(len(top_countries)), top_countries['total_burned_area'])
    plt.xlabel('Country')
    plt.ylabel('Total Burned Area (km²)')
    plt.title(f'Top {top_n} Countries by Total Burned Area (2002-2023)')
    plt.xticks(range(len(top_countries)), top_countries.index, rotation=45, ha='right')
    
    for i, bar in enumerate(bars):
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.0f}',
                ha='center', va='bottom', fontsize=8)
    
    plt.tight_layout()
    plt.savefig('top_countries_burned_area.png', dpi=300, bbox_inches='tight')
    plt.show()

# --------------------------
# Function: Create Regional Heatmap
# --------------------------
# This function generates a heatmap showing fire activity by country and land cover type
# for the top N countries by total burned area.
def create_regional_heatmap(df, top_n=30):
    """
    Create a heatmap showing fire activity by region and land cover type
    """
    fire_columns = ['forest', 'savannas', 'shrublands_grasslands', 'croplands', 'other']
    country_totals = df.groupby('country')[fire_columns].sum()
    country_totals['total'] = country_totals.sum(axis=1)
    top_countries = country_totals.nlargest(top_n, 'total')
    
    heatmap_data = top_countries[fire_columns]
    
    plt.figure(figsize=(12, 16))
    
    sns.heatmap(heatmap_data, 
                annot=True, 
                fmt='.0f', 
                cmap='YlOrRd',
                cbar_kws={'label': 'Burned Area (km²)'})
    
    plt.title(f'Fire Activity Heatmap: Top {top_n} Countries by Land Cover Type')
    plt.xlabel('Land Cover Type')
    plt.ylabel('Country')
    plt.tight_layout()
    plt.savefig('regional_fire_heatmap.png', dpi=300, bbox_inches='tight')
    plt.show()

# --------------------------
# Function: Create World Fire Map Simulation
# --------------------------
# This function simulates a world map by arranging the top 50 countries in a grid.
# The circle size and color represent burned area intensity.
def create_world_fire_map_simulation(country_summary):
    plt.figure(figsize=(16, 10))
    
    top_50_countries = country_summary.head(50)
    
    n_cols = 10
    n_rows = int(np.ceil(len(top_50_countries) / n_cols))
    
    x_positions = []
    y_positions = []
    sizes = []
    
    for i, (country, data) in enumerate(top_50_countries.iterrows()):
        row = i // n_cols
        col = i % n_cols
        
        x_positions.append(col)
        y_positions.append(n_rows - row)
        
        size = max(50, min(1000, data['total_burned_area'] / 1000))
        sizes.append(size)
    
    scatter = plt.scatter(x_positions, y_positions, 
                         s=sizes, 
                         c=[country_summary.loc[country, 'total_burned_area'] for country in top_50_countries.index],
                         cmap='YlOrRd',
                         alpha=0.7,
                         edgecolors='black',
                         linewidth=0.5)
    
    for i, country in enumerate(top_50_countries.index):
        plt.annotate(country[:3], 
                    (x_positions[i], y_positions[i]),
                    ha='center', va='center',
                    fontsize=8,
                    fontweight='bold')
    
    plt.colorbar(scatter, label='Total Burned Area (km²)')
    plt.title('Global Fire Activity: Country-Level Overview (2002-2023)\nCircle size and color represent burned area intensity')
    plt.xlabel('Grid Position (West ← → East)')
    plt.ylabel('Grid Position (South ← → North)')
    
    plt.xticks([])
    plt.yticks([])
    
    plt.tight_layout()
    plt.savefig('world_fire_map_simulation.png', dpi=300, bbox_inches='tight')
    plt.show()

# --------------------------
# Main Function
# --------------------------
# This is the entry point of the program. It:
# - Loads the dataset
# - Creates summaries and analyses
# - Generates all visualizations
# - Prints final summary statistics
# - Handles errors gracefully
def main():
    csv_file_path = 'MCD64A1_burned_area_full_dataset_2002-2023.csv'
    
    try:
        df = load_and_process_fire_data(csv_file_path)
        
        print("\nCreating country summary...")
        country_summary = create_country_fire_summary(df)
        
        print("Creating yearly trend analysis...")
        yearly_summary = create_yearly_trend_analysis(df)
        
        print("Creating land cover analysis...")
        land_cover_totals = create_land_cover_analysis(df)
        
        print("\nGenerating visualizations...")
        
        print("1. Top countries by burned area...")
        plot_top_countries_burned_area(country_summary)
        
        print("2. Regional heatmap...")
        create_regional_heatmap(df)
        
        print("3. World fire map simulation...")
        create_world_fire_map_simulation(country_summary)
        
        print("\n" + "="*50)
        print("FIRE DATA ANALYSIS SUMMARY")
        print("="*50)
        print(f"Total countries analyzed: {df['country'].nunique()}")
        print(f"Years covered: {df['year'].min()} - {df['year'].max()}")
        print(f"Total global burned area: {country_summary['total_burned_area'].sum():,.0f} km²")
        
        print(f"\nTop 10 Countries by Total Burned Area:")
        for i, (country, data) in enumerate(country_summary.head(10).iterrows(), 1):
            print(f"{i:2d}. {country}: {data['total_burned_area']:,.0f} km²")
        
        print(f"\nBurned Area by Land Cover Type:")
        for land_type, area in land_cover_totals.sort_values(ascending=False).items():
            percentage = (area / land_cover_totals.sum()) * 100
            print(f"  {land_type}: {area:,.0f} km² ({percentage:.1f}%)")
        
        print(f"\nAll visualizations have been saved as PNG files!")
        print("Files created:")
        print("- top_countries_burned_area.png")
        print("- land_cover_distribution.png") 
        print("- yearly_fire_trends.png")
        print("- regional_fire_heatmap.png")
        print("- world_fire_map_simulation.png")
        
    except FileNotFoundError:
        print(f"Error: Could not find the file '{csv_file_path}'")
        print("Please make sure the CSV file is in the same directory as this script.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()