# ResearchMind

A Streamlit research app using Tavily search and web scraping.

## Run locally

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Create a `.env` file from `.env.example` and add your keys:

```bash
TAVILY_API_KEY=your_tavily_api_key_here
```

3. Start the app:

```bash
streamlit run app.py
```

## Deploy

This project is easiest to deploy on Streamlit Community Cloud.

1. Push this folder to GitHub.
2. In Streamlit Cloud, create a new app from the repo.
3. Set the main file path to:

```text
app.py
```

4. Add this secret in Streamlit Cloud:

```toml
TAVILY_API_KEY = "your_tavily_api_key_here"
```

5. Deploy the app.

The app needs internet access at runtime for Tavily search and website scraping.
