import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from PIL import Image

# Set random seed for reproducibility
np.random.seed(42)

# Generate realistic synthetic data for business context
# Product categories and their performance metrics (e.g., monthly revenue)
categories = ['Electronics', 'Clothing', 'Home & Garden', 'Sports', 
              'Books', 'Toys', 'Health & Beauty', 'Automotive']
revenue = np.random.normal(45000, 15000, len(categories))
revenue = np.maximum(revenue, 10000)  # Ensure minimum revenue
revenue = np.round(revenue, 0)

# Create DataFrame
df = pd.DataFrame({
    'Category': categories,
    'Revenue': revenue
})

# Sort by revenue for better visualization
df = df.sort_values('Revenue', ascending=True).reset_index(drop=True)

# Set professional Seaborn style
sns.set_style("whitegrid")
sns.set_context("notebook", font_scale=1.2)

# Create figure with exact pixel dimensions: 512x512 pixels
# Using figsize in inches: 512 pixels / 64 dpi = 8 inches
plt.figure(figsize=(8, 8))

# Create barplot with professional styling
ax = sns.barplot(
    data=df,
    x='Revenue',
    y='Category',
    hue='Category',
    palette='viridis',  # Professional color palette
    orient='h',  # Horizontal bars for better category label readability
    legend=False  # Remove legend since categories are already on y-axis
)

# Customize the chart with professional styling
ax.set_title(
    'Monthly Revenue by Product Category',
    fontsize=16,
    fontweight='bold',
    pad=20
)
ax.set_xlabel('Revenue ($)', fontsize=13, fontweight='semibold')
ax.set_ylabel('Product Category', fontsize=13, fontweight='semibold')

# Add value labels on bars
for i, (idx, row) in enumerate(df.iterrows()):
    ax.text(
        row['Revenue'] + 1000,
        i,
        f'${row["Revenue"]:,.0f}',
        va='center',
        fontsize=10,
        fontweight='semibold'
    )

# Customize grid for better readability
ax.grid(axis='x', alpha=0.3, linestyle='--')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color('#cccccc')
ax.spines['bottom'].set_color('#cccccc')

# Adjust layout
plt.tight_layout()

# Save chart as PNG with exactly 512x512 pixels
# dpi=64 with figsize=(8,8) gives 8*64 = 512 pixels
# Remove bbox_inches='tight' to ensure exact dimensions
plt.savefig('chart.png', dpi=64, bbox_inches='tight', facecolor='white', pad_inches=0)
plt.close()

# Resize to exactly 512x512 pixels using PIL to ensure precise dimensions
img = Image.open('chart.png')
img_resized = img.resize((512, 512), Image.Resampling.LANCZOS)
img_resized.save('chart.png', 'PNG')
print("Chart saved as chart.png (exactly 512x512 pixels)")

