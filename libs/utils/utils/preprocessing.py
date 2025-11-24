import pandas as pd
import os
import numpy as np
import json
from collections import Counter
from sklearn.utils import shuffle

# Load the JSON file
def gpt_answer_preprocessing(disruptive_represent,consolidating_represent, notexposed_represent,classification_name ):
    grouped_data_disruptive= Counter(disruptive_represent[classification_name ] )
    grouped_data_consolidating = Counter(consolidating_represent[classification_name ] )
    # grouped_data_exposed= Counter(exposed_represent_how[classification_name ] )
    grouped_data_notexposed = Counter(notexposed_represent[classification_name ])
    
    total_count_disruptive = sum(grouped_data_disruptive.values())
    
    
    total_count_consolidating = sum(grouped_data_consolidating.values())
    
    # total_count_exposed = sum(grouped_data_exposed.values())
    
    
    total_count_notexposed = sum(grouped_data_notexposed.values())

    categories = list(grouped_data_notexposed.keys())
    gpt_proportions = {"disruptive": {} ,"consolidating": {},"notexposed": {}}
    for category in categories:
    
        gpt_proportion_notexposed = grouped_data_notexposed[category]/total_count_notexposed
            
        gpt_proportion_consolidating = grouped_data_consolidating[category]/total_count_consolidating
        gpt_proportion_disruptive = grouped_data_disruptive[category]/total_count_disruptive  
        gpt_proportions["disruptive"][category] = gpt_proportion_disruptive
        gpt_proportions["consolidating"][category] = gpt_proportion_consolidating
        gpt_proportions["notexposed"][category] = gpt_proportion_notexposed
    return gpt_proportions


def null_model_zscore(disruptive_df, consolidating_df, notexposed_df, category_name):
    ## Define the number of permutations
    n_permutations = 1000
    results = []
    all_data = pd.concat([
        disruptive_df.assign(Category='Disruptive'),
        consolidating_df.assign(Category='Consolidating'),
        notexposed_df.assign(Category='Not Exposed')
    ])

    
    # Perform the shuffling n_permutations times
    for _ in range(n_permutations):
        shuffled_how = shuffle(all_data[category_name].values)
        all_data['shuffled'] = shuffled_how
        counts = all_data.groupby('Category')['shuffled'].value_counts(normalize=True).unstack(fill_value=0)
        results.append(counts)
   
    # Convert list of DataFrames to a single DataFrame
    results_df = pd.concat(results)
    mean_results = results_df.groupby(level=0).mean()
    std_results = results_df.groupby(level=0).std()
    # Calculate Z-scores
    # Get the original data
    original_counts = all_data.groupby('Category')[category_name].value_counts(normalize=True).unstack(fill_value=0)

    z_scores = (original_counts - mean_results) / std_results

    return z_scores
    
