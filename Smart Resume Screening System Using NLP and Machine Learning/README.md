# 📄 AI-Powered Resume Analyzer & Skill Gap Finder

A beginner-friendly Python application that uses NLP to analyze resumes against job descriptions, identify skill gaps, and provide actionable improvement suggestions.

## 🎯 Features

- **Resume Upload**: Support for PDF and DOCX formats
- **Text Extraction**: Automatic text extraction from uploaded resumes
- **NLP Processing**: Advanced text preprocessing and skill extraction
- **Smart Matching**: Intelligent matching with synonym handling (e.g., ML = Machine Learning)
- **Match Percentage**: Calculate how well your resume matches the job description
- **Skill Analysis**: 
  - ✅ Matched skills (skills present in both resume and JD)
  - ❌ Missing skills (skills in JD but not in resume)
- **Improvement Suggestions**: Actionable tips to improve your resume
- **Clean UI**: Simple, intuitive Streamlit interface
- **Sample JDs**: Pre-loaded sample job descriptions for testing

## 🛠️ Tech Stack

- **Python 3.8+**
- **Streamlit**: Web UI framework
- **pdfplumber**: PDF text extraction
- **python-docx**: DOCX text extraction
- **NLTK**: Natural Language Processing
- **scikit-learn**: TF-IDF vectorization for keyword extraction
- **spaCy**: Advanced NLP (optional enhancement)

## 📁 Project Structure

```
resume-analyzer/
├── app.py                      # Main Streamlit application
├── utils/
│   ├── __init__.py
│   ├── text_extractor.py      # PDF/DOCX text extraction
│   ├── nlp_processor.py       # NLP processing & skill extraction
│   └── matcher.py             # Resume-JD matching logic
├── data/
│   └── sample_jds.txt         # Sample job descriptions
├── requirements.txt           # Python dependencies
└── README.md                  # This file
```


## 🚀 Setup & Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Step-by-Step Setup

1. **Clone or download this project**
   ```bash
   cd resume-analyzer
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   streamlit run app.py
   ```

5. **Open in browser**
   - The app will automatically open in your default browser
   - If not, navigate to: `http://localhost:8501`

## 📖 How to Use

1. **Upload Resume**: Click "Browse files" and select your resume (PDF or DOCX)
2. **Add Job Description**: Paste the complete job description in the text area
   - Or check "Use sample job description" to test with a sample
3. **Click Analyze**: Press the "🔍 Analyze Match" button
4. **Review Results**:
   - Match percentage score
   - Matched skills (what you have)
   - Missing skills (what you need)
   - Improvement suggestions

## 🧠 How the Matching Logic Works

### 1. Text Extraction
- Extracts text from PDF using `pdfplumber`
- Extracts text from DOCX using `python-docx`
- Cleans and normalizes the extracted text

### 2. NLP Processing
- **Tokenization**: Breaks text into individual words
- **Stopword Removal**: Removes common words (the, is, at, etc.)
- **Skill Extraction**: Identifies technical skills using pattern matching
- **Synonym Handling**: Normalizes variations (JS → JavaScript, ML → Machine Learning)

### 3. Matching Algorithm
```
Match % = (Matched Skills / Total JD Skills) × 100
```

- Extracts skills from both resume and job description
- Uses TF-IDF to identify important keywords
- Compares skill sets to find matches and gaps
- Calculates percentage based on overlap

### 4. Skill Database
The system recognizes 50+ common technical skills including:
- Programming languages (Python, Java, JavaScript, etc.)
- Frameworks (React, Django, Flask, etc.)
- Databases (SQL, MongoDB, PostgreSQL, etc.)
- Cloud platforms (AWS, Azure, GCP)
- DevOps tools (Docker, Kubernetes, CI/CD)
- Data Science (Machine Learning, TensorFlow, Pandas)


## 📊 Example Output

```
Match Score: 75%
Matched Skills: 12
Missing Skills: 4

✅ Matched Skills:
- python
- django
- rest api
- sql
- git
- docker
- aws
- machine learning
- postgresql
- ci/cd
- flask
- agile

❌ Missing Skills:
- kubernetes
- mongodb
- react
- microservices

💡 Improvement Suggestions:
- Good match! Consider adding a few more relevant skills.
- Priority skills to add: kubernetes, mongodb, react, microservices
- Tip: Use exact keywords from the job description in your resume.
- Tip: Quantify your achievements with numbers and metrics.
```

## 🧪 Testing with Sample Data

The project includes sample job descriptions in `data/sample_jds.txt`:
1. Senior Python Developer
2. Full Stack Developer
3. Data Scientist

To test:
1. Upload any resume
2. Check "Use sample job description"
3. Click "Analyze Match"

## 🔧 Common Issues & Fixes

### Issue 1: NLTK Data Not Found
**Error**: `Resource punkt not found`
**Fix**: The app automatically downloads NLTK data on first run. If it fails:
```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
```

### Issue 2: PDF Extraction Fails
**Error**: `Error extracting PDF`
**Fix**: 
- Ensure PDF is not password-protected
- Try converting to DOCX format
- Check if PDF contains actual text (not scanned images)

### Issue 3: Port Already in Use
**Error**: `Address already in use`
**Fix**: 
```bash
streamlit run app.py --server.port 8502
```

### Issue 4: Module Not Found
**Error**: `ModuleNotFoundError: No module named 'xxx'`
**Fix**: 
```bash
pip install -r requirements.txt --upgrade
```


## 🎓 Code Explanation

### app.py
Main Streamlit application that:
- Sets up the UI layout
- Handles file uploads
- Displays analysis results
- Coordinates between different modules

### utils/text_extractor.py
Handles document processing:
- `extract_text_from_pdf()`: Extracts text from PDF files
- `extract_text_from_docx()`: Extracts text from Word documents
- `clean_text()`: Removes extra whitespace and special characters

### utils/nlp_processor.py
NLP processing engine:
- `preprocess_text()`: Tokenizes and removes stopwords
- `extract_skills()`: Identifies technical skills using pattern matching
- `extract_keywords_tfidf()`: Extracts important keywords using TF-IDF
- `SKILL_SYNONYMS`: Dictionary mapping skill variations to canonical forms

### utils/matcher.py
Matching logic:
- `calculate_match_score()`: Compares resume and JD, calculates match percentage
- `generate_suggestions()`: Creates personalized improvement recommendations

## 🚀 Future Enhancements

### Phase 1 (Easy)
- [ ] Export results as PDF report
- [ ] Save analysis history
- [ ] Support for more file formats (TXT, RTF)
- [ ] Dark mode toggle

### Phase 2 (Moderate)
- [ ] Resume scoring system (0-100)
- [ ] ATS (Applicant Tracking System) compatibility check
- [ ] Keyword density analysis
- [ ] Resume formatting suggestions
- [ ] Multiple resume comparison

### Phase 3 (Advanced)
- [ ] AI-powered resume rewriting suggestions
- [ ] Integration with job boards (LinkedIn, Indeed)
- [ ] Cover letter generator
- [ ] Interview question predictor based on JD
- [ ] Salary estimation based on skills
- [ ] Career path recommendations

## 🤝 Contributing

Feel free to fork this project and submit pull requests for improvements!

## 📝 License

This project is open source and available for educational purposes.

## 👨‍💻 Author

Built as a learning project for AI-powered resume analysis.

## 🙏 Acknowledgments

- NLTK for NLP capabilities
- Streamlit for the amazing web framework
- pdfplumber for PDF processing
- The open-source community

---

**Happy Job Hunting! 🎯**

For questions or issues, please create an issue in the repository.
