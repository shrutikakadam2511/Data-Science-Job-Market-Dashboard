import pandas as pd
from collections import Counter
import re

def clean_and_analyze(path="jobs.csv"):
    df = pd.read_csv(path)
    df.dropna(inplace=True)

    # Extract skills using simple keyword matching
    skills_keywords = ['python', 'sql', 'excel', 'machine learning', 'nlp', 'deep learning', 'tableau']
    
    df['skills'] = df['summary'].apply(lambda x: [skill for skill in skills_keywords if skill in x.lower()])
    
    # Count skills
    all_skills = [skill for sublist in df['skills'] for skill in sublist]
    skill_freq = dict(Counter(all_skills))

    return df, skill_freq
