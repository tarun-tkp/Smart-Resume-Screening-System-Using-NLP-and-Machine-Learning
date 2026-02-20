"""
NLP Processor Module
Handles text preprocessing and skill extraction using NLP techniques
"""

import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer


# Download required NLTK data (will be handled in app initialization)
def download_nltk_data():
    """Download required NLTK datasets"""
    try:
        nltk.data.find('tokenizers/punkt')
    except LookupError:
        nltk.download('punkt', quiet=True)
    
    try:
        nltk.data.find('corpora/stopwords')
    except LookupError:
        nltk.download('stopwords', quiet=True)


# Common tech skills and their synonyms
SKILL_SYNONYMS = {
    'machine learning': ['ml', 'machine learning', 'machinelearning'],
    'artificial intelligence': ['ai', 'artificial intelligence'],
    'javascript': ['js', 'javascript', 'java script'],
    'typescript': ['ts', 'typescript'],
    'python': ['python', 'py'],
    'rest api': ['rest', 'restful', 'rest api', 'api'],
    'database': ['db', 'database', 'databases'],
    'sql': ['sql', 'mysql', 'postgresql', 'postgres'],
    'nosql': ['nosql', 'mongodb', 'cassandra', 'dynamodb'],
    'react': ['react', 'reactjs', 'react.js'],
    'angular': ['angular', 'angularjs'],
    'vue': ['vue', 'vuejs', 'vue.js'],
    'node': ['node', 'nodejs', 'node.js'],
    'docker': ['docker', 'containerization'],
    'kubernetes': ['k8s', 'kubernetes'],
    'aws': ['aws', 'amazon web services'],
    'azure': ['azure', 'microsoft azure'],
    'gcp': ['gcp', 'google cloud'],
    'ci/cd': ['ci/cd', 'cicd', 'continuous integration'],
    'git': ['git', 'github', 'gitlab', 'version control'],
}


# Common technical skills to look for
COMMON_SKILLS = [
    # Programming Languages
    'python', 'java', 'javascript', 'typescript', 'c++', 'c#', 'ruby', 'php', 
    'swift', 'kotlin', 'go', 'rust', 'scala', 'r',
    
    # Web Technologies
    'html', 'css', 'react', 'angular', 'vue', 'node', 'express', 'django', 
    'flask', 'spring', 'asp.net', 'jquery',
    
    # Databases
    'sql', 'mysql', 'postgresql', 'mongodb', 'redis', 'elasticsearch', 
    'oracle', 'dynamodb', 'cassandra',
    
    # Cloud & DevOps
    'aws', 'azure', 'gcp', 'docker', 'kubernetes', 'jenkins', 'terraform', 
    'ansible', 'ci/cd', 'git',
    
    # Data Science & AI
    'machine learning', 'deep learning', 'nlp', 'computer vision', 'tensorflow', 
    'pytorch', 'scikit-learn', 'pandas', 'numpy', 'data analysis',
    
    # Other Skills
    'agile', 'scrum', 'rest api', 'graphql', 'microservices', 'testing', 
    'unit testing', 'api', 'linux', 'bash'
]


def preprocess_text(text):
    """
    Preprocess text: lowercase, tokenize, remove stopwords
    
    Args:
        text: Input text string
        
    Returns:
        list: List of processed tokens
    """
    # Convert to lowercase
    text = text.lower()
    
    # Tokenize
    tokens = word_tokenize(text)
    
    # Remove stopwords and short tokens
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token not in stop_words and len(token) > 2]
    
    return tokens


def extract_skills(text):
    """
    Extract technical skills from text using pattern matching and NLP
    
    Args:
        text: Input text string
        
    Returns:
        set: Set of extracted skills
    """
    text_lower = text.lower()
    found_skills = set()
    
    # Check for each common skill
    for skill in COMMON_SKILLS:
        # Use word boundaries to avoid partial matches
        pattern = r'\b' + re.escape(skill) + r'\b'
        if re.search(pattern, text_lower):
            found_skills.add(skill)
    
    # Check for synonyms and normalize
    for canonical, synonyms in SKILL_SYNONYMS.items():
        for synonym in synonyms:
            pattern = r'\b' + re.escape(synonym) + r'\b'
            if re.search(pattern, text_lower):
                found_skills.add(canonical)
                break
    
    return found_skills


def extract_keywords_tfidf(text, top_n=20):
    """
    Extract important keywords using TF-IDF
    
    Args:
        text: Input text string
        top_n: Number of top keywords to extract
        
    Returns:
        list: List of important keywords
    """
    try:
        # Preprocess
        tokens = preprocess_text(text)
        processed_text = ' '.join(tokens)
        
        # TF-IDF vectorization
        vectorizer = TfidfVectorizer(max_features=top_n, ngram_range=(1, 2))
        tfidf_matrix = vectorizer.fit_transform([processed_text])
        
        # Get feature names (keywords)
        keywords = vectorizer.get_feature_names_out()
        
        return list(keywords)
    except:
        return []
