import streamlit as st
from langchain_community.document_loaders import WebBaseLoader

from chains import Chain
from portfolio import Portfolio
from utils import clean_text

def create_streamlit_app(llm, portfolio, clean_text):
    st.set_page_config(layout="wide", page_title="Cold Email Generator", page_icon="📧")

    # --- Custom CSS for Styling ---
    st.markdown(
        """
        <style>
        body {
            font-family: 'Arial', sans-serif;
        }
        .stButton>button {
            background-color: #4CAF50; /* Green */
            border: none;
            color: white;
            padding: 10px 20px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            border-radius: 5px;
        }
        .stExpanderContent {
            border: 1px solid #ddd;
            padding: 10px;
            border-radius: 5px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # --- App Title ---
    st.title("📧 Cold Email Generator")

    with st.form("input_form"):
        url_input = st.text_input("Paste the Job URL Here:", value="https://jobs.nike.com/job/R-33460")
        submit_button = st.form_submit_button("Generate Email")

    if submit_button:
        try:
            with st.spinner("Loading and processing..."):
                loader = WebBaseLoader([url_input])
                data = clean_text(loader.load().pop().page_content)
                portfolio.load_portfolio()
                jobs = llm.extract_jobs(data)

            if jobs:
                for job in jobs:
                    with st.expander(f"Job Description: {job.get('title', 'N/A')}"):
                        st.write(job.get('description', 'No description available.'))
                        skills = job.get('skills', [])
                        links = portfolio.query_links(skills)
                        email = llm.write_mail(job, links)
                        st.code(email, language='markdown')
            else:
                st.warning("No jobs found on the provided page.")

        except Exception as e:
            st.error(f"An Error Occurred: {e}")


if __name__ == "__main__":
    chain = Chain()
    portfolio = Portfolio()
    create_streamlit_app(chain, portfolio, clean_text)


