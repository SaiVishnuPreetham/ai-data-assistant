# 📊 AI Data Analysis Assistant

> An interactive Streamlit-powered data analysis tool that leverages Google's Gemini AI to provide instant, actionable insights from your data through natural language questions.

---

## 🚀 Overview

AI Data Analysis Assistant is a Python-based web application that enables users to upload data files (CSV, Excel, JSON), apply interactive filters, visualize data with customizable charts, and ask natural language questions to receive AI-powered analysis. The application uses **Google Gemini 2.0 Flash** via LangChain for intelligent data interpretation.

---

## ✨ Features

### 📁 Multi-Format Data Upload
- **CSV files** with automatic encoding detection (UTF-8, ISO-8859-1, Latin1, CP1252, UTF-16)
- **Excel files** (`.xls`, `.xlsx`) via `openpyxl`
- **JSON files** with smart normalization for nested structures (arrays, dictionaries)

### 🔍 Smart Interactive Filtering
- Sidebar-based filtering for numeric columns
- Dynamic range sliders with min/max detection
- Real-time data preview with highlighted maximum values

### 🤖 AI-Powered Conversational Analysis
- Ask natural language questions about your data
- Powered by **Google Gemini 2.0 Flash** LLM (temperature: 0.2 for consistent results)
- Receives structured insights including:
  - Key trends
  - Anomalies detection
  - Recommended actions
  - Suggested next analysis steps

### 📈 Interactive Visualization
- **Chart Types**: Histogram, Line Chart, Bar Chart
- Customizable X and Y axis selection
- Color picker for chart customization
- Built with `matplotlib`

### 🗃️ Session History
- Maintains conversation history across queries
- Review all previous questions, answers, and associated data
- Expandable history entries with data previews

---

## 📦 Tech Stack

| Component | Technology |
|-----------|------------|
| Frontend | [Streamlit](https://streamlit.io/) |
| AI/LLM | [Google Gemini 2.0 Flash](https://ai.google.dev/) via LangChain |
| Data Processing | [Pandas](https://pandas.pydata.org/) |
| Visualization | [Matplotlib](https://matplotlib.org/) |
| File Parsing | `openpyxl` (Excel), `pyarrow`, `json` |

---

## 📋 Requirements

```
streamlit
langchain
langchain-google-genai
tabulate
pandas
matplotlib
plotly
pyarrow
openpyxl
python-dotenv
```

---

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/SaiVishnuPreetham/ai-data-assistant.git
   cd ai-data-assistant
   ```

2. **Create and activate a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

---

## ⚙️ Configuration

### Set up your Google API Key

You need a Google API Key with access to the Gemini API.

**Option 1: Environment Variable (`.env` file)**
Create a `.env` file in the project root:
```
GOOGLE_API_KEY=your_google_api_key_here
```

**Option 2: Streamlit Secrets**
Create `.streamlit/secrets.toml`:
```toml
GOOGLE_API_KEY = "your_google_api_key_here"
```

> ⚠️ **Security Note**: Never commit your `.env` file or API keys to version control. The `.gitignore` is already configured to exclude `.env` files.

---

## ▶️ Usage

1. **Start the application**
   ```bash
   streamlit run app.py
   ```

2. **Open your browser** at `http://localhost:8501`

3. **Upload your data file** (CSV, XLS/XLSX, or JSON)

4. **Apply filters** using the sidebar (for numeric columns)

5. **Ask a question** in natural language (e.g., "What are the top sales trends?")

6. **Click "Analyze"** to receive AI-generated insights

7. **View visualizations** and customize chart settings

8. **Review history** of all your previous analyses

---

## 🔄 Application Workflow

```
┌─────────────────────────────────────────────────────────────┐
│                    Upload Data File                         │
│              (CSV / Excel / JSON)                           │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│              Auto-detect Encoding & Parse                   │
│         (Tries multiple encodings for robustness)           │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│               Apply Interactive Filters                     │
│           (Sidebar with numeric column sliders)             │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│              Ask Natural Language Question                  │
│         (e.g., "Show sales trends by region")               │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│               AI Analysis via Gemini LLM                    │
│    (Trends, Anomalies, Recommendations, Next Steps)         │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│              View Results & Visualizations                  │
│         (Histogram / Line / Bar with custom colors)         │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                Review Analysis History                      │
│           (All queries and responses saved)                 │
└─────────────────────────────────────────────────────────────┘
```

---

## 📂 Project Structure

```
ai-data-assistant/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── .gitignore          # Git ignore rules
├── .env                # API key configuration (not tracked)
└── README.md           # Project documentation
```

---

## 🔧 Key Functions

| Function | Description |
|----------|-------------|
| `init_llm()` | Initializes Google Gemini 2.0 Flash LLM with API key validation |
| `try_read_csv()` | Attempts CSV parsing with multiple encodings |
| `try_read_json()` | Parses JSON with smart normalization for nested data |
| `load_data()` | Unified data loader supporting CSV, Excel, and JSON |
| `create_filters()` | Creates sidebar filters for numeric columns |
| `create_visualization()` | Renders customizable matplotlib charts |
| `main()` | Main application flow with session state management |

---

## 📝 Example Questions

- "What are the key trends in this dataset?"
- "Identify any anomalies or outliers"
- "Compare sales performance across regions"
- "Summarize the top 10 products by revenue"
- "What patterns exist in customer behavior?"

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 👤 Author

**SaiVishnuPreetham**

- GitHub: [@SaiVishnuPreetham](https://github.com/SaiVishnuPreetham)
