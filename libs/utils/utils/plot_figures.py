import matplotlib.pyplot as plt
import numpy as np

# Data


def zscore_original_characteristics(human_proportions, gpt_proportions, category_name,categories, SAVE_LOCATION):

    if category_name == 'Agumentation Potential':
        x = np.array([0,1,2,4,5,6,8,9,10])  # Label locations
        
        
        fig, ax = plt.subplots(figsize=(6, 5.2))

    else:
        x = np.array([0,1,2,4,5,6])  # Label locations
        fig, ax = plt.subplots(figsize=(6, 5))
    width = 0.5 # Bar width
    
    
    
    # Define colors for each category
    colors = [
        '#D73027',  # Disruptive
        '#4575B4',  # Consolidating
        '#8E7CC3'   # Not Exposed
    ]
    
    # Plot bars for Human annotations
    rects1 = ax.bar(x - width/2, human_proportions, width, label='Human', color=colors, alpha=0.5)
    
    # Plot bars for GPT annotations
    rects2 = ax.bar(x + width/2, gpt_proportions, width, label='GPT', color=colors)
    
    # Labeling and aesthetics
    ax.set_ylabel('Z-Score', fontsize=15)
    ax.set_title(category_name, fontsize=20)
    if category_name == 'Agumentation Potential':
        ax.set_xticks([x[1] , x[4], x[7]  ])
        print("here")
    
    else:
        ax.set_xticks([x[1] , x[4] ])

    ax.set_xticklabels(categories, fontsize=15)
    ax.set_yticks([-3,-2,-1,0,1,2,3 ])
    ax.yaxis.grid(True)  # Add horizontal grid lines for better readability
    
    # Add labels to bars
    # for rect in rects1 + rects2:
    #     height = rect.get_height()
    #     ax.annotate(f'{height:.2f}',
    #                 xy=(rect.get_x() + rect.get_width() / 2, height),
    #                 xytext=(0, 3),  # Vertical offset
    #                 textcoords="offset points",
    #                 ha='center', va='bottom',
    #                 fontsize=10)
    
    # Add legend and adjust layout
    # ax.legend(fontsize=12)
    fig.tight_layout()
    
    plt.savefig(SAVE_LOCATION)
    plt.show()


def plot_category(index,df,left_char, right_char,index_name):
    max_length = 3.9
    colors = [
    '#4575B4',  # Consolidating
    '#D73027',  # Disruptive
    '#8E7CC3'   # Not Exposed
    ]

    category = df.iloc[index]
    
    fig, ax = plt.subplots(figsize=(10, 2))
    ax.set_xlim(-max_length - 1, max_length + 1)
    ax.set_ylim(-0.5, 0.5)
    ax.axis('off')  # Turn off the axis
    
    # Add a vertical line at x=0
    ax.axvline(x=0, color='gray', linestyle='--', linewidth=2, zorder=0)

    # Plot combined arrow with thicker border and white fill
    zscore_99 = 3.891 #(99.99)
    ax.annotate('', xy=(-zscore_99, 0), xytext=(2, 0),
                arrowprops=dict(headwidth=30, headlength=25, linewidth=10, facecolor=colors[index], edgecolor=colors[index]), zorder=1)
    ax.annotate('', xy=(zscore_99, 0), xytext=(-2, 0),
                arrowprops=dict(headwidth=30, headlength=25, linewidth=10, facecolor=colors[index], edgecolor=colors[index]), zorder=1)

    # Add inverse triangle marker for positive values only
    if category[left_char] > 0:
        if abs(category[left_char]) > zscore_99:
            ax.plot(-zscore_99, 0.3, marker='v', color='black', markersize=50,zorder=2)
        else:
            ax.plot(-category[left_char], 0.3, marker='v', color='black', markersize=50,zorder=2)
    if category[right_char] > 0:
        if abs(category[right_char]) > zscore_99:
            ax.plot(zscore_99, 0.3, marker='v', color='black', markersize=50,zorder=2)
        else:
            ax.plot(category[right_char], 0.3, marker='v', color='black', markersize=50,zorder=2)
    
    plt.tight_layout()
    plt.savefig(f'../results/figures/{index_name}_{left_char}_{right_char}_combined_impact_03142025.png', dpi=300,bbox_inches = 'tight')  # Save the figure
    plt.show()



    
