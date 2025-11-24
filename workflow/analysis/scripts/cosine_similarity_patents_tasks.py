"""
Purpose: 
    matching tasks with patents based on their cosine similarity
Input:
    - argv[1] : embedding_patents
    
Ouput:
    - task index which is closest to each patent

Author: Munjung Kim
"""

import pandas as pd
import logging
import sys
import pickle 

def normalize_rows(X):
    return X / np.linalg.norm(X, axis=1, keepdims=True)

if __name__ == "__main__":

    PATENT_TABLE_PATH = sys.argv[1]
    CPC_DATASET = sys.argv[2]
    
    SAVE_FILE_PATENT_CPC_DICT = sys.argv[3]
    SAVE_FILE_PATENT_YEAR_DICT = sys.argv[4]
    SAVE_FILE_PAPER_ID_PATENT_ID_DICT = sys.argv[5]

    logging.basicConfig(filename = 'cpc_match_patent_meta.log',level=logging.INFO, format='%(asctime)s %(message)s')

    batch_size = 10000  # You may need to adjust this based on your memory

    # Results placeholder
    closest_indices = np.zeros(patent_embedding_normalized.shape[0], dtype=int)
    closest_values = np.zeros(patent_embedding_normalized.shape[0])
    
    # Process in batches
    for start in tqdm(range(0, patent_embedding_normalized.shape[0], batch_size)):
        end = start + batch_size
        if end > patent_embedding_normalized.shape[0]:
            end = patent_embedding_normalized.shape[0]
        
        # Compute cosine similarity for the batch
        batch_cosine_similarity = np.dot(patent_embedding_normalized[start:end], task_embedding_normalized .T)
        
        # Find the index of the max similarity for each vector in the batch
        batch_indices = np.argmax(batch_cosine_similarity, axis=1)
        batch_values = np.max(batch_cosine_similarity, axis=1)
        
        # Store results
        closest_indices[start:end] = batch_indices
        closest_values[start:end] = batch_values
    
    # Optionally, do something with the results here
    # e.g., save them, print them, etc.
    
    # You might want to verify by printing some results
    print("Sample of results:")
    print(closest_indices[:10])
    print(closest_values[:10])

    