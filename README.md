# The Potential Impact of Disruptive AI Innovations on U.S. Occupations

# Files

## Main Notebook Files

| **File Name**                                                   | **Description**                                                                         | **Location**         |
|-----------------------------------------------------------------|-----------------------------------------------------------------------------------------|----------------------|
| `01-Tasks_Disruptive_vs_Consolidating.ipynb`                    | Classifying patents and their impacted tasks                                            | `notebook/`          |
| `02-Louvain_Representative.ipynb`                               | Selecting representative tasks for comparing human vs GPT                               | `notebook/`          |
| `03-Comparing_GPT_vs_Human_Annotations.ipynb`                   | Comparing annotation results from GPT vs human                                          | `notebook/`          |
| `04-Disruptive_AI_Impact_on_Different_Tasks.ipynb`              | Analyzing the features of tasks impacted by disruptive and consolidating AI             | `notebook/`          |
| `05-Disruptive_vs_Consolidating_Industry.ipynb`                 | Comparing disruptive vs consolidating AI impacts on tasks across different industries   | `notebook/`          |
| `06-Disruptive_AI_Geographical_Analysis.ipynb`                  | Analyzing the geographical distribution of disruptive AI impacts on tasks               | `notebook/`          |
| `07-Vacancy Rate.ipynb`                  | Analyzing the relationship between industry-level vacancy rates and exposure to disruptive and consolidating AI              | `notebook/`          |


## Python File Descriptions

| **File Name**                           | **Description**                                                 | **Location**             |
|-----------------------------------------|-----------------------------------------------------------------|--------------------------|
| `Disruption.py`                         | Script for generating the disruption index                      | `workflow/preprocessing` |
| `embedding.py`                          | Script for creating embeddings                                  | `workflow/preprocessing` |
| `cosine_similarity_patents_tasks.py`    | Calculating cosine similarity between patent embeddings and task embeddings | `workflow/analysis`     |


## Library

libs/utils

codes including plotting figures and generating null model


# Data



| **File Name**                           | **Description**                                                 | **Location**             |
|-----------------------------------------|-----------------------------------------------------------------|--------------------------|
| `ai_patents_keywrods_alicpc_07092024.csv`                          | AI Related Patents                                  |`data/processed` |
| `tasks_matched_with_ai_patent_keywords_alicpc.csv`    | Tasks Matched to AI Related Patents | `data/processed`   |
| `finalized_gpt_response....`    | GPT respones for mental, collaborative, and unpredictable classification of Whole Tasks (file name indicates the characteristics) | `data/processed/GPT_Whole_Tasks`   |
| `finalized_gpt_response....`    | GPT respones for mental, collaborative, and unpredictable classification of Representative Tasks(file name indicates the characteristics_ | `data/processed/GPT_VS_Human`   |
| `ai_related_patents_cosine_similarity_task.npy`    | Cosine Similarity Between Tasks and Best Matched AI Patent | `data/processed/Embeddings`   |
| `ai_patents_matched_id.npy`    | AI Patent ID Matched to Tasks | `data/processed/Embeddings`   |
| `consolidating_tasks.csv`    | Tasks Classified as Impacted by Consolidating Tasks | `data/processed/ClassifiedTasks`   |
| `disruptive_tasks.csv`    | Tasks Classified as Impacted by Disruptive Tasks | `data/processed/ClassifiedTasks`   |



