# 📊 InsightIQ — An AI-Powered E-Commerce BI Dashboard

An intelligent Business Intelligence platform built on the Olist Brazilian 
E-Commerce dataset, combining interactive analytics, machine learning, 
and AI-powered natural language querying to make data more accessible and actionable.

## 🌐 Live Demo
👉 [Click here to view the live dashboard](https://insightiq-7yu2fhb69wowgatgvd6ztg.streamlit.app/)

---

## 📌 Project Overview
InsightIQ was developed as a DSC 550 Master's Project at the University of Massachusetts Dartmouth, applied to 100,000 real e-commerce orders from the Olist Brazilian marketplace (2016–2018).

While working on this dataset, I realized that traditional dashboards usually show *what is happening*, but not *why it is happening*. This project was built to bridge that gap by combining analytics, machine learning, and AI-driven interaction into a single system.

The goal was not just to visualize e-commerce data, but to make it more **interactive, interpretable, and useful for decision-making**.

---

## 💡 Key Design Decisions
- Instead of building a static dashboard, I chose an interactive BI approach using Streamlit to allow real-time exploration.
- I integrated a machine learning model to go beyond visualization and provide predictive insights.
- I included a natural language query feature so that even non-technical users can interact with the data.

---

## ⚠️ Challenges & Learning
- Handling multiple relational tables required careful joins and data preparation.
- Initial model performance was not satisfactory until feature selection and tuning were improved.
- Translating technical outputs into meaningful business insights was one of the most valuable parts of this project.

---

## ✨ Features
- 📈 **Business Overview** — Monthly revenue and order volume trends
- 🚚 **Delivery Performance** — Delivery time analysis and distribution
- ⭐ **Customer Reviews** — Review score distribution and insights
- 🔮 **Delay Predictor** — ML model to predict delivery delays (~90.25% accuracy)
- 🤖 **AI Insights** — Natural language Q&A powered by OpenAI GPT

---

## 📊 Key Insights
- Delivery delays are influenced by logistics, location, and order volume
- Customer reviews are strongly linked to delivery performance
- Seasonal trends impact both revenue and order behavior

These insights highlight how combining analytics with machine learning can support better operational and business decisions.

---

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

---

## 📊 Dataset
- **Source:** Olist Brazilian E-Commerce Public Dataset (Kaggle)
- **Size:** 100,000 orders across 9 relational tables
- **Period:** 2016 to 2018
- **Link:** https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce

---

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

---

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

---

## 👩‍💻 Author
**Sree Likhitha Ninarapu** — MS in Data Science, UMass Dartmouth  
- GitHub: [@Likhitha-0398](https://github.com/Likhitha-0398)

---

## 📄 License
This project is for academic purposes — DSC 550 Master's Project, UMass Dartmouth.
