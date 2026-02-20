"""
AI-Powered Resume Analyzer & Skill Gap Finder
Main Streamlit Application
"""

import streamlit as st
from utils.text_extractor import extract_text_from_pdf, extract_text_from_docx, clean_text
from utils.nlp_processor import download_nltk_data
from utils.matcher import calculate_match_score, generate_suggestions


# Page configuration
st.set_page_config(
    page_title="Resume Analyzer",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded"
)


# Initialize NLTK data
@st.cache_resource
def initialize_nltk():
    """Download required NLTK data on first run"""
    download_nltk_data()


def main():
    """Main application function"""
    
    # Initialize NLTK
    initialize_nltk()
    
    # Header
    st.title("📄 AI-Powered Resume Analyzer")
    st.markdown("### Match your resume against job descriptions and find skill gaps")
    st.markdown("---")
    
    # Sidebar
    with st.sidebar:
        st.header("📋 About")
        st.info(
            "This tool helps you:\n"
            "- Upload your resume (PDF/DOCX)\n"
            "- Compare it with a job description\n"
            "- Get match percentage\n"
            "- Identify skill gaps\n"
            "- Receive improvement suggestions"
        )
        
        st.header("🔧 How It Works")
        st.markdown(
            """
            1. **Upload** your resume
            2. **Paste** the job description
            3. **Analyze** to see results
            4. **Review** matched & missing skills
            5. **Improve** your resume
            """
        )
        
        st.header("💡 Tips")
        st.markdown(
            """
            - Use keywords from the JD
            - Quantify achievements
            - Highlight relevant skills
            - Tailor for each application
            """
        )
    
    # Main content area
    col1, col2 = st.columns(2)
    
    # Column 1: Resume Upload
    with col1:
        st.header("1️⃣ Upload Resume")
        uploaded_file = st.file_uploader(
            "Choose your resume file",
            type=['pdf', 'docx'],
            help="Upload your resume in PDF or DOCX format"
        )
        
        resume_text = ""
        if uploaded_file is not None:
            try:
                # Extract text based on file type
                if uploaded_file.name.endswith('.pdf'):
                    resume_text = extract_text_from_pdf(uploaded_file)
                elif uploaded_file.name.endswith('.docx'):
                    resume_text = extract_text_from_docx(uploaded_file)
                
                # Clean text
                resume_text = clean_text(resume_text)
                
                st.success(f"✅ Resume uploaded: {uploaded_file.name}")
                
                # Show preview
                with st.expander("📄 Preview Resume Text"):
                    st.text_area("Resume Content", resume_text, height=200, disabled=True)
                    
            except Exception as e:
                st.error(f"❌ Error processing resume: {str(e)}")
    
    # Column 2: Job Description Input
    with col2:
        st.header("2️⃣ Job Description")
        
        # Sample JD option
        use_sample = st.checkbox("Use sample job description", value=False)
        
        if use_sample:
            sample_jd = """
Senior Python Developer

Requirements:
- 5+ years of experience in Python development
- Strong knowledge of Django and Flask frameworks
- Experience with REST API development
- Proficiency in SQL and NoSQL databases (PostgreSQL, MongoDB)
- Familiarity with cloud platforms (AWS, Azure)
- Experience with Docker and Kubernetes
- Knowledge of CI/CD pipelines
- Strong understanding of machine learning concepts
- Experience with Git version control
- Excellent problem-solving skills
- Bachelor's degree in Computer Science or related field

Nice to have:
- Experience with React or Angular
- Knowledge of microservices architecture
- Familiarity with Agile/Scrum methodologies
            """
            jd_text = st.text_area(
                "Job Description",
                value=sample_jd,
                height=300,
                help="Paste the complete job description here"
            )
        else:
            jd_text = st.text_area(
                "Paste Job Description",
                height=300,
                placeholder="Paste the complete job description here...",
                help="Include all requirements, qualifications, and skills"
            )
    
    # Analyze button
    st.markdown("---")
    col_btn1, col_btn2, col_btn3 = st.columns([1, 1, 1])
    with col_btn2:
        analyze_button = st.button("🔍 Analyze Match", type="primary", use_container_width=True)
    
    # Analysis Results
    if analyze_button:
        if not resume_text:
            st.error("❌ Please upload a resume first!")
        elif not jd_text.strip():
            st.error("❌ Please provide a job description!")
        else:
            with st.spinner("🔄 Analyzing your resume..."):
                # Calculate match
                results = calculate_match_score(resume_text, jd_text)
                suggestions = generate_suggestions(results)
                
                st.markdown("---")
                st.header("📊 Analysis Results")
                
                # Match Score
                match_pct = results['match_percentage']
                ml_score = results['ml_match_score']
                col_score1, col_score2, col_score3, col_score4 = st.columns(4)
                
                with col_score1:
                    st.metric("Skill Match", f"{match_pct}%")
                with col_score2:
                    st.metric("ML Match Score", f"{ml_score}%")
                with col_score3:
                    st.metric("Matched Skills", results['total_matched'])
                with col_score4:
                    st.metric("Missing Skills", len(results['missing_skills']))
                
                # Progress bar - use ML score for visual
                if ml_score >= 80:
                    bar_color = "green"
                elif ml_score >= 60:
                    bar_color = "orange"
                else:
                    bar_color = "red"
                
                st.progress(ml_score / 100)
                
                # Explanation of scores
                with st.expander("ℹ️ Understanding the Scores"):
                    st.markdown("""
                    **Skill Match**: Percentage based on matched keywords and skills
                    
                    **ML Match Score**: AI-powered score using TF-IDF and cosine similarity
                    - Analyzes overall content similarity
                    - Considers context and word importance
                    - More holistic than keyword matching
                    
                    💡 A good match typically has both scores above 60%
                    """)
                
                # Detailed Results
                st.markdown("---")
                
                col_res1, col_res2 = st.columns(2)
                
                with col_res1:
                    st.subheader("✅ Matched Skills")
                    if results['matched_skills']:
                        for skill in results['matched_skills']:
                            st.markdown(f"- ✓ {skill}")
                    else:
                        st.info("No matched skills found")
                
                with col_res2:
                    st.subheader("❌ Missing Skills")
                    if results['missing_skills']:
                        for skill in results['missing_skills']:
                            st.markdown(f"- ✗ {skill}")
                    else:
                        st.success("No missing skills!")
                
                # Suggestions
                st.markdown("---")
                st.subheader("💡 Improvement Suggestions")
                for suggestion in suggestions:
                    st.markdown(f"- {suggestion}")
                
                # Additional Details
                with st.expander("📈 Detailed Analysis"):
                    st.write("**Your Resume Skills:**")
                    st.write(", ".join(results['resume_skills']) if results['resume_skills'] else "None detected")
                    
                    st.write("\n**Job Description Requirements:**")
                    st.write(", ".join(results['jd_skills']) if results['jd_skills'] else "None detected")


if __name__ == "__main__":
    main()
