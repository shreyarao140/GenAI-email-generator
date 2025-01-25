# GenAI-email-generator
email generator using Llama3.3 LLM, Langchain, Chromadb and Streamlit

# 📧 Cold Email Generator

## Overview

This application streamlines the process of crafting tailored cold emails for job applications. It leverages the power of language models and web scraping to:

1. **Extract Job Details:** Given a job posting URL, the app automatically scrapes and extracts key information like job description, required skills, and experience level.
2. **Match with Portfolio:** It then compares the extracted skills with your own portfolio of projects and experiences, identifying relevant links to showcase.
3. **Generate Personalized Emails:** Using a large language model, the app generates a professional cold email tailored to the specific job posting, highlighting your skills and relevant experience, and including links to your portfolio.

## Features

- **Easy to Use:** Simply paste the job posting URL and let the app do the rest.
- **Time-Saving:**  Automates the tedious parts of cold emailing, allowing you to focus on personalization.
- **Effective:** Increases your chances of standing out by tailoring your message to each specific job.

## Technologies Used

1. **Streamlit:**  For building the interactive web application.
2. **LangChain:** For orchestrating interactions with the language model and other components.
3. **ChromaDB:** For creating a vector database of your portfolio, enabling semantic search based on skills. 
4. **Llama 3.3 70B Versatile (via ChatGroq):** For language understanding, job extraction, and email generation. 
5. **Pandas:**  For data manipulation and working with the portfolio data.
6. **Beautiful Soup/Requests (optional):** If needed for more advanced web scraping. 

## Installation and Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/[your-username]/cold-email-generator.git 
   cd cold-email-generator
## Set-up
To get started we first need to get an API_KEY from here: https://console.groq.com/keys. Inside app/.env update the value of GROQ_API_KEY with the API_KEY you created.

To get started, first install the dependencies using:
pip install -r requirements.txt

Run the streamlit app:
streamlit run app/main.py
