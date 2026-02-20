# 🚀 Quick Start Guide

## For Windows Users

### Option 1: Automated Setup (Easiest)
1. Double-click `setup.bat`
2. Wait for installation to complete
3. Run these commands:
   ```
   venv\Scripts\activate
   streamlit run app.py
   ```

### Option 2: Manual Setup
```bash
# Create virtual environment
python -m venv venv

# Activate it
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

## For Mac/Linux Users

```bash
# Create virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

## First Time Usage

1. The app will open in your browser at `http://localhost:8501`
2. On first run, NLTK will download required data (takes ~30 seconds)
3. Upload a resume or use the sample JD to test
4. Click "Analyze Match" to see results

## Testing the App

1. Check "Use sample job description" checkbox
2. Upload any resume (or create a dummy one)
3. Click "Analyze Match"
4. You should see match percentage and skill analysis

## Troubleshooting

**App won't start?**
- Make sure Python 3.8+ is installed: `python --version`
- Try: `pip install --upgrade streamlit`

**NLTK errors?**
- Run: `python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"`

**Port already in use?**
- Run: `streamlit run app.py --server.port 8502`

## Need Help?

Check the full README.md for detailed documentation and troubleshooting.
