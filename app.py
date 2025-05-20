import os
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import json
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Configure Streamlit
st.set_page_config(page_title="AI Data Assistant", page_icon="🤖", layout="wide")
st.title("📊 Interactive AI Data Analysis Assistant")

# Initialize Gemini LLM
def init_llm():
    api_key = os.getenv("GOOGLE_API_KEY") or st.secrets.get("GOOGLE_API_KEY")
    if not api_key:
        st.error("Missing Google API Key. Set GOOGLE_API_KEY in environment variables.")
        st.stop()
    return ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0.2)

# Data loading

def try_read_csv(uploaded_file):
    encodings = ["utf-8", "ISO-8859-1", "latin1", "cp1252", "utf-16"]
    for enc in encodings:
        uploaded_file.seek(0)
        try:
            return pd.read_csv(uploaded_file, encoding=enc)
        except Exception:
            continue
    raise ValueError("Unable to read CSV file with common encodings.")

def try_read_json(uploaded_file):
    encodings = ["utf-8", "ISO-8859-1", "latin1", "cp1252", "utf-16"]
    for enc in encodings:
        uploaded_file.seek(0)
        try:
            content = uploaded_file.read().decode(enc)
            data = json.loads(content)
            if isinstance(data, list):
                return pd.json_normalize(data)
            elif isinstance(data, dict):
                for k, v in data.items():
                    if isinstance(v, list):
                        return pd.json_normalize(v)
                return pd.json_normalize(data)
            return pd.DataFrame(data)
        except Exception:
            continue
    raise ValueError("Unable to read JSON file with common encodings.")

def load_data(uploaded_file):
    try:
        filename = uploaded_file.name.lower()
        if filename.endswith('.csv'):
            return try_read_csv(uploaded_file)
        elif filename.endswith(('.xls', '.xlsx')):
            uploaded_file.seek(0)
            return pd.read_excel(uploaded_file)
        elif filename.endswith('.json'):
            return try_read_json(uploaded_file)
        else:
            st.error("Unsupported file format")
            return None
    except Exception as e:
        st.error(f"Error loading file: {str(e)}")
        return None

# Interactive filters sidebar
def create_filters(df):
    with st.sidebar:
        st.header("🔍 Data Filters")
        numeric_cols = df.select_dtypes(include='number').columns
        if len(numeric_cols) > 0:
            col = st.selectbox("Filter numeric column", numeric_cols)
            min_val, max_val = df[col].min(), df[col].max()
            filter_range = st.slider(f"Range for {col}", min_val, max_val, (min_val, max_val))
            return df[(df[col] >= filter_range[0]) & (df[col] <= filter_range[1])]
        return df

# Visualization controls
def create_visualization(df):
    st.subheader("📈 Interactive Visualization")
    cols = st.columns(2)
    with cols[0]:
        chart_type = st.selectbox("Chart Type", ["Histogram", "Line", "Bar"])
        x_axis = st.selectbox("X Axis", df.columns)
    with cols[1]:
        y_axis = st.selectbox("Y Axis", df.columns) if chart_type != "Histogram" else None
        color = st.color_picker("Chart Color", "#4f8bff")
    
    fig, ax = plt.subplots()
    try:
        if chart_type == "Histogram":
            ax.hist(df[x_axis].dropna(), bins=20, color=color)
        elif chart_type == "Line":
            ax.plot(df[x_axis], df[y_axis] if y_axis else None, color=color)
        elif chart_type == "Bar":
            ax.bar(df[x_axis], df[y_axis] if y_axis else None, color=color)
        st.pyplot(fig)
    except Exception as e:
        st.warning(f"Visualization error: {str(e)}")

# Main application flow
def main():
    # Initialize session state
    if "history" not in st.session_state:
        st.session_state.history = []

    # File upload form
    with st.form("data_input"):
        uploaded_file = st.file_uploader("Upload Data File", type=["csv", "xls", "xlsx", "json"])
        question = st.text_area("Ask about your data:", height=100)
        submitted = st.form_submit_button("Analyze")

    if submitted and uploaded_file:
        df = load_data(uploaded_file)
        for col in df.columns:
            try:
                df[col] = pd.to_numeric(df[col], errors='coerce')
            except Exception:
                pass
        if df is not None:
            # Data filtering
            df_filtered = create_filters(df)
            
            # Data preview
            with st.expander("🔍 Preview Filtered Data"):
                st.dataframe(df_filtered.style.highlight_max(axis=0), use_container_width=True)

            # Generate analysis
            llm = init_llm()
            summary = f"""
            Columns: {', '.join(df_filtered.columns)}
            Shape: {df_filtered.shape}
            Sample Data: {df_filtered.head(3).to_markdown()}
            """
            
            response = llm.invoke(f"""
            Analyze this data for: {question}
            
            Data Summary:
            {summary}
            
            Provide insights with:
            - Key trends
            - Anomalies
            - Recommended actions
            - Next analysis steps
            """).content

            # Store in history
            st.session_state.history.append({
                "question": question,
                "answer": response,
                "data": df_filtered.copy()
            })

            # Display analysis
            st.subheader("📝 Analysis Results")
            st.markdown(response)

            # Visualization
            create_visualization(df_filtered)

    # Conversation history
    if st.session_state.history:
        st.subheader("🗃️ Analysis History")
        for i, entry in enumerate(st.session_state.history[::-1]):
            with st.expander(f"Analysis #{len(st.session_state.history)-i}: {entry['question'][:50]}..."):
                st.markdown(entry["answer"])
                st.dataframe(entry["data"].head(3))

if __name__ == "__main__":
    main()
