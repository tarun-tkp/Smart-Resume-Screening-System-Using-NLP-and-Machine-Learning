"""
Matcher Module
Handles matching logic between resume and job description
"""

from utils.nlp_processor import extract_skills, extract_keywords_tfidf, preprocess_text
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re


def calculate_ml_match_score(resume_text, jd_text):
    """
    Calculate ML-based match score using TF-IDF and cosine similarity
    
    Args:
        resume_text: Resume text content
        jd_text: Job description text content
        
    Returns:
        float: Match score as percentage (0-100)
    """
    try:
        # Preprocess texts: lowercase and clean
        resume_clean = resume_text.lower()
        jd_clean = jd_text.lower()
        
        # Remove special characters but keep spaces
        resume_clean = re.sub(r'[^a-z0-9\s]', ' ', resume_clean)
        jd_clean = re.sub(r'[^a-z0-9\s]', ' ', jd_clean)
        
        # Remove extra whitespace
        resume_clean = ' '.join(resume_clean.split())
        jd_clean = ' '.join(jd_clean.split())
        
        # Create TF-IDF vectorizer with stopword removal
        vectorizer = TfidfVectorizer(
            stop_words='english',
            max_features=100,
            ngram_range=(1, 2)  # Use unigrams and bigrams
        )
        
        # Fit and transform both texts
        tfidf_matrix = vectorizer.fit_transform([resume_clean, jd_clean])
        
        # Calculate cosine similarity
        similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
        
        # Convert to percentage
        ml_score = round(similarity * 100, 2)
        
        return ml_score
    except Exception as e:
        # Return 0 if any error occurs
        return 0.0


def calculate_match_score(resume_text, jd_text):
    """
    Calculate match percentage between resume and job description
    
    Args:
        resume_text: Resume text content
        jd_text: Job description text content
        
    Returns:
        dict: Dictionary containing match results
    """
    # Extract skills from both texts
    resume_skills = extract_skills(resume_text)
    jd_skills = extract_skills(jd_text)
    
    # Extract additional keywords using TF-IDF
    resume_keywords = set(extract_keywords_tfidf(resume_text, top_n=15))
    jd_keywords = set(extract_keywords_tfidf(jd_text, top_n=15))
    
    # Combine skills and keywords
    resume_features = resume_skills.union(resume_keywords)
    jd_features = jd_skills.union(jd_keywords)
    
    # Calculate matches
    matched_features = resume_features.intersection(jd_features)
    missing_features = jd_features - resume_features
    
    # Calculate match percentage
    if len(jd_features) > 0:
        match_percentage = (len(matched_features) / len(jd_features)) * 100
    else:
        match_percentage = 0
    
    # Calculate ML-based match score using TF-IDF + cosine similarity
    ml_match_score = calculate_ml_match_score(resume_text, jd_text)
    
    # Separate skills and keywords for better display
    matched_skills = matched_features.intersection(jd_skills)
    missing_skills = missing_features.intersection(jd_skills)
    
    return {
        'match_percentage': round(match_percentage, 2),
        'ml_match_score': ml_match_score,  # New ML-based score
        'matched_skills': sorted(list(matched_skills)),
        'missing_skills': sorted(list(missing_skills)),
        'total_jd_requirements': len(jd_features),
        'total_matched': len(matched_features),
        'resume_skills': sorted(list(resume_skills)),
        'jd_skills': sorted(list(jd_skills))
    }


def generate_suggestions(match_results):
    """
    Generate improvement suggestions based on match results
    
    Args:
        match_results: Dictionary from calculate_match_score
        
    Returns:
        list: List of suggestion strings
    """
    suggestions = []
    match_pct = match_results['match_percentage']
    ml_score = match_results.get('ml_match_score', 0)
    missing_skills = match_results['missing_skills']
    
    # Overall assessment based on ML score
    if ml_score >= 80:
        suggestions.append("✅ Excellent match! Your resume aligns very well with the job requirements.")
    elif ml_score >= 60:
        suggestions.append("👍 Good match! Your resume shows strong alignment with the job.")
    elif ml_score >= 40:
        suggestions.append("⚠️ Moderate match. Consider tailoring your resume more closely to the JD.")
    else:
        suggestions.append("❌ Low match. Significant resume optimization needed for this role.")
    
    # Skill-based assessment
    if match_pct >= 70:
        suggestions.append(f"🎯 Strong skill coverage: {match_pct}% of required skills matched.")
    elif match_pct >= 50:
        suggestions.append(f"📊 Decent skill coverage: {match_pct}% matched, but room for improvement.")
    else:
        suggestions.append(f"📉 Limited skill coverage: Only {match_pct}% matched. Focus on adding key skills.")
    
    # Missing skills suggestions
    if missing_skills:
        priority_skills = list(missing_skills)[:5]  # Top 5 missing skills
        suggestions.append(f"🎯 Priority skills to add: {', '.join(priority_skills)}")
        
        if len(missing_skills) > 5:
            suggestions.append(f"📚 Also consider learning: {', '.join(list(missing_skills)[5:10])}")
    
    # General tips
    suggestions.append("💡 Tip: Use exact keywords from the job description in your resume.")
    suggestions.append("💡 Tip: Quantify your achievements with numbers and metrics.")
    suggestions.append("💡 Tip: Tailor your resume for each job application.")
    
    return suggestions
