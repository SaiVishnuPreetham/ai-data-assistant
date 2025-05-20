# AI Data Analysis Assistant
---
## 🚀 Overview

AI Data Analysis Assistant is a Streamlit-powered tool that lets you upload CSV, Excel, or JSON data, filter and visualize it, and ask natural language questions for instant, actionable insights using Google Gemini LLM.

## 🖥️ Features

- Multi-format Upload: CSV, XLS/XLSX, JSON (auto encoding detection)

- Smart Filtering: Interactive sidebar for numeric columns

- Conversational Analysis: Ask questions, get LLM-powered insights (trends, anomalies, recommendations)

- Visualization: Choose chart type, axes, and color

- Session History: Review all previous queries and results
  
---

## 📦 Installation
```
git clone https://github.com/your-username/your-repo.git

cd your-repo

pip install -r requirements.txt
```
---

## ⚡ Usage

Set your Google API Key

- Create a `.env` file in the project root:
  ```
  GOOGLE_API_KEY=your_google_api_key_here
  ```
- **Do NOT share or commit your `.env` file.**

Run the App:
```
streamlit run app.py
```
---

## Workflow

- Upload your data file

- Filter and preview data

- Ask a question (e.g., “Show top sales trends”)

- View AI-generated analysis and charts

- Review analysis history
