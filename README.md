# 📊 InsightIQ — AI-Powered E-Commerce BI Dashboard

An intelligent Business Intelligence platform built on the Olist Brazilian 
E-Commerce dataset, combining interactive analytics, machine learning, 
and AI-powered natural language querying.

## 🌐 Live Demo
👉 [Click here to view the live dashboard](https://your-streamlit-url.streamlit.app)

## 📌 Project Overview
InsightIQ is a DSC 550 Master's Project at the University of Massachusetts 
Dartmouth. It demonstrates an end-to-end data science workflow applied to 
100,000 real e-commerce orders from the Olist Brazilian marketplace (2016-2018).

## ✨ Features
- 📈 **Business Overview** — Monthly revenue and order volume trends
- 🚚 **Delivery Performance** — Delivery time analysis and distribution
- ⭐ **Customer Reviews** — Review score distribution and insights
- 🔮 **Delay Predictor** — ML model to predict delivery delays (92.66% accuracy)
- 🤖 **AI Insights** — Natural language Q&A powered by OpenAI GPT

## 🛠️ Tech Stack
| Technology | Purpose |
|---|---|
| Python 3.11 | Core language |
| Streamlit | Dashboard framework |
| Plotly | Interactive charts |
| SQLite | Relational database |
| Pandas | Data manipulation |
| Scikit-learn | ML model (Random Forest) |
| OpenAI GPT API | Natural language Q&A |

## 📊 Dataset
- **Source:** Olist Brazilian E-Commerce Public Dataset (Kaggle)
- **Size:** 100,000 orders across 9 relational tables
- **Period:** 2016 to 2018
- **Link:** https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce

## 🚀 Run Locally
```bash
# Clone the repository
git clone https://github.com/Likhitha-0398/insightiq.git
cd insightiq

# Create conda environment
conda create -n insightiq python=3.11
conda activate insightiq

# Install dependencies
pip install -r requirements.txt

# Add your OpenAI API key
echo "OPENAI_API_KEY=your_key_here" > .env

# Run the app
streamlit run app.py
```

## 📁 Project Structure
```
insightiq/
├── app.py                  # Main Streamlit entry point
├── load_data.py            # One-time data loading script
├── train_model.py          # ML model training script
├── pages/
│   ├── 1_Overview.py       # Revenue and orders dashboard
│   ├── 2_Delivery.py       # Delivery performance page
│   ├── 3_Reviews.py        # Customer reviews page
│   ├── 4_Predictor.py      # ML delay predictor
│   └── 5_AI_Insights.py    # OpenAI Q&A page
├── utils/
│   ├── db.py               # Database query utility
│   └── ai.py               # OpenAI integration
├── data/raw/               # Olist CSV files
└── requirements.txt        # Python dependencies
```

## 👩‍💻 Author
**Sree Likhitha** — MS in Data Science, UMass Dartmouth
- GitHub: [@Likhitha-0398](https://github.com/Likhitha-0398)

## 📄 License
This project is for academic purposes — DSC 550 Master's Project, UMass Dartmouth.
```