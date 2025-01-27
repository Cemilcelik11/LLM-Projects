# Cold Email Generator

## Credits
This Github repo is prepared by coding alongside the video of the YouTube channel "Codebasics". The video provides an excellent end-to-end guide for building an LLM project using Llama 3.1.

## Story
Your company employs software engineers with different specialities like Python, Java, Golang etc. As a marketing employee, you have some other companies in target by checking for which roles they hire. Then you send them a cold e-mail or LinkedIn DM expressing the capabilities of your company to provide their needs. You explain your company, your employees and the project portfolios your comapny made so far. All you have to do is to put the URL of that job posting you want to send a cold e-mail for into our searchbar.   

## Step-by-Step Implementation
  - We get the text for a specific job posting of a target company by using WebBaseLoader of langchain_community, it is basically web scraping.
  - We then feed this text to a prompt using PromptTemplate and then JsonOutputParser of langchain_core to extract role, experience, skills, and job description info in JSON format.
  - We store Techstack information with related portfolio URLs in chromadb vector store.
  - Afterwards we prepare another prompt, this time for writing the e-mail itself, the inputs to the prompt are the job description text and the portfolio links.
  - We show the generated e-mail in Streamlit.
  - For inference, we use GroqCloud because it is fast.
    ![image](https://github.com/user-attachments/assets/c61ebe6d-1780-4e26-b445-7ec38431ec75)

