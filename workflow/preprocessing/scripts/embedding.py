"""
Purpose: 
    Embedding tasks and abstract of patents
Input:
    - argv[1] : path to the tasks or patents
    - argv[2] : path to the embedding file
    - argv[3] : type of the input ("task", "patent")
    
Ouput:
    - Embedding numpy file 

Author: Ali
Edited by Munjung Kim
"""


import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer
import logging
import sys
from time import time 
if __name__ == "__main__":
    
    logging.basicConfig(filename = 'Embedding.log',level=logging.INFO, format='%(asctime)s %(message)s')
    

    TEXT_FILE = sys.argv[1]
    EMBEDDING_FILE = sys.argv[2]
    TEXT_TYPE = sys.argv[3]


    model = SentenceTransformer(
        'sentence-transformers/sentence-t5-xl',
        cache_folder='/10TBdrive/MJ/.cache/huggingface/',
    )

    logging.info("Reading file")

    if TEXT_TYPE == "task":
        task_ratings = pd.read_csv(TEXT_FILE, sep='\t').query('`Scale ID` == "IM"')
        task_statements = pd.read_csv('datasets/db_26_3_text/Task Statements.txt', sep='\t')
        jobs = pd.read_csv('datasets/db_26_3_text/Occupation Data.txt', sep='\t')
        jobs['SOC Code'] = jobs['O*NET-SOC Code'].str[:7]

        tasks = pd.merge(
        task_ratings,
        task_statements[['O*NET-SOC Code', 'Task ID', 'Task']],
        how='left',
        on=['O*NET-SOC Code', 'Task ID'])


        pool = model.start_multi_process_pool([ 'cuda:1', 'cuda:2', 'cuda:3', 'cuda:4', 'cuda:5', 'cuda:6', 'cuda:7'])
        task_embeddings = model.encode_multi_process(tasks['Task'].values, pool)
        model.stop_multi_process_pool(pool)
        np.save('datasets/task_embeddings_26_3.npy', task_embeddings)


    elif TEXT_TYPE == "patent":

        patent_table = pd.read_csv(TEXT_FILE)
        start_time = time()
        pool = model.start_multi_process_pool(['cuda:0', 'cuda:1', 'cuda:2', 'cuda:3', 'cuda:4', 'cuda:5', 'cuda:6', 'cuda:7'])

        patent_table = patent_table[patent_table['abstract'].notna()]

        
        emb = model.encode_multi_process(patent_table['abstract'].tolist(), pool)
        model.stop_multi_process_pool(pool)
        # emb = model.encode(df['abstract'].to_list())
        end_time = time()
        elapsed_time = (end_time - start_time) / 60
        print(f"Elapsed time = {elapsed_time:.2f} mins")
    
        logging.info("Saving the embeddings for")

        # np.save('datasets/r-embeddings.npy', emb)
        np.save(EMBEDDING_FILE, emb)


