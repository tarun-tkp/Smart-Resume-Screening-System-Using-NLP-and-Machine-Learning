# 🧪 Testing Guide

## How to Test the Application

### Test 1: Basic Functionality
1. Start the app: `streamlit run app.py`
2. Check "Use sample job description"
3. Create a simple text file with these skills:
   ```
   John Doe
   Software Developer
   
   Skills: Python, Django, SQL, Git, Docker, AWS
   
   Experience:
   - Developed REST APIs using Django
   - Worked with PostgreSQL databases
   - Deployed applications on AWS
   ```
4. Save as `test_resume.txt` and upload
5. Click "Analyze Match"
6. Expected: ~50-60% match with matched and missing skills displayed

### Test 2: High Match Score
Create a resume with ALL skills from the sample JD:
```
Senior Python Developer

Skills:
Python, Django, Flask, REST API, SQL, PostgreSQL, MongoDB, 
AWS, Azure, Docker, Kubernetes, CI/CD, Machine Learning, 
Git, React, Microservices, Agile, Scrum

Experience:
- 5+ years Python development
- Built REST APIs with Django and Flask
- Deployed on AWS and Azure
- Implemented CI/CD pipelines
- Applied machine learning models
```
Expected: 80-90% match

### Test 3: Low Match Score
Create a resume with unrelated skills:
```
Graphic Designer

Skills: Photoshop, Illustrator, InDesign, Figma, Sketch

Experience:
- Created marketing materials
- Designed logos and branding
```
Expected: 0-10% match

### Test 4: Synonym Recognition
Test if the system recognizes synonyms:
- Use "ML" instead of "Machine Learning"
- Use "JS" instead of "JavaScript"
- Use "K8s" instead of "Kubernetes"

Expected: System should recognize these as matches

## Sample Resume Text for Copy-Paste Testing

```
JOHN DOE
Senior Software Engineer

SKILLS
Programming: Python, JavaScript, Java, C++
Web: React, Node.js, Django, Flask, HTML, CSS
Database: PostgreSQL, MongoDB, MySQL, Redis
Cloud: AWS, Docker, Kubernetes
Tools: Git, Jenkins, CI/CD, Agile

EXPERIENCE
Senior Developer at Tech Corp (2020-Present)
- Developed microservices using Python and Django
- Built REST APIs serving 1M+ requests/day
- Implemented machine learning models for recommendation system
- Deployed applications on AWS using Docker and Kubernetes
- Led team of 5 developers using Agile methodology

Software Engineer at StartupXYZ (2018-2020)
- Created full-stack web applications with React and Node.js
- Managed PostgreSQL and MongoDB databases
- Implemented CI/CD pipelines with Jenkins
- Collaborated using Git version control

EDUCATION
Bachelor of Science in Computer Science
University of Technology, 2018
```

## Expected Results for Sample Resume

When matched against "Senior Python Developer" JD:
- Match Score: 75-85%
- Matched Skills: python, django, flask, rest api, sql, postgresql, mongodb, aws, docker, kubernetes, ci/cd, machine learning, git, react, microservices, agile
- Missing Skills: azure (if in JD)

## Validation Checklist

- [ ] App starts without errors
- [ ] File upload works for PDF
- [ ] File upload works for DOCX
- [ ] Sample JD loads correctly
- [ ] Analysis completes without errors
- [ ] Match percentage displays
- [ ] Matched skills list shows
- [ ] Missing skills list shows
- [ ] Suggestions appear
- [ ] UI is responsive and clean
- [ ] NLTK data downloads automatically
- [ ] Synonym recognition works

## Performance Testing

- Upload a 5-page resume → Should process in < 5 seconds
- Paste a 1000-word JD → Should analyze in < 3 seconds
- Multiple analyses → Should maintain speed

## Edge Cases to Test

1. Empty resume file
2. Resume with only images (scanned PDF)
3. Very short JD (1 sentence)
4. Very long JD (5000+ words)
5. Special characters in text
6. Non-English text
7. Resume with no technical skills

## Debugging Tips

If something doesn't work:
1. Check browser console for errors (F12)
2. Check terminal for Python errors
3. Verify all dependencies installed: `pip list`
4. Try restarting the app
5. Clear Streamlit cache: Delete `.streamlit` folder
