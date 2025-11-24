"""
Purpose: 
    matching cpc dataset with patent
Input:
    - argv[1] : path to patent metadata
    - argv[2] : path to cpc patent matching
    - argv[3] : save path
    
Ouput:
    - patent metadataset containing cpc codes

Author: Munjung Kim
"""

import pandas as pd
import logging
import sys
import pickle 

if __name__ == "__main__":

    PATENT_TABLE_PATH = sys.argv[1]
    CPC_DATASET = sys.argv[2]
    
    SAVE_FILE_PATENT_CPC_DICT = sys.argv[3]
    SAVE_FILE_PATENT_YEAR_DICT = sys.argv[4]
    SAVE_FILE_PAPER_ID_PATENT_ID_DICT = sys.argv[5]

    logging.basicConfig(filename = 'cpc_match_patent_meta.log',level=logging.INFO, format='%(asctime)s %(message)s')
    
    patent_table = pd.read_csv(PATENT_TABLE_PATH )
    cpc_patent_table = pd.read_csv(CPC_DATASET,sep= '\t')
    
    patent_year_dict = patent_table.groupby('paper_id')['year'].apply(list).to_dict()
    paper_id_patent_id_dict = patent_table.groupby('paper_id')['patent_id'].apply(list).to_dict()
    patent_cpc_subclass_dict = cpc_patent_table.groupby('patent_id')['cpc_subclass'].apply(list).to_dict()
    

    # logging.info("cpc_codse_attaching")

    # patent_table['cpc_codes'] = patent_table['patent_id'].apply(lambda x: patent_cpc_subclass_dict[x])

    # patent_table = patent_table[['patent_id','cpc_codes', 'type','country','date','year', 'title','kind','paper_id']]

    # logging.info("file saving")
    # patent_table.to_csv(SAVE_FILE_PATENT_CPC,index=False)
    
    logging.info("dict saving")
    with open(SAVE_FILE_PATENT_CPC_DICT, 'wb') as f:
        pickle.dump(patent_cpc_subclass_dict, f)

    with open(SAVE_FILE_PAPER_ID_PATENT_ID_DICT, 'wb') as f:
        pickle.dump(paper_id_patent_id_dict, f)
        
    with open(SAVE_FILE_PATENT_YEAR_DICT, 'wb') as f:
        pickle.dump(patent_year_dict, f)

    
    