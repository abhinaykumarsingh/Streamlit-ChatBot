# APISM Assist

Lightweight Streamlit chat UI for API Subscription Manager (APISM).  
Provides a static set of quick prompts at the top and a WhatsApp-style chat (user on right, assistant on left). Designed to call a backend agent via `agent_client.get_agent_response`.

## Features

- Static, compact quick-prompts list (top of page)
- Default assistant greeting: "Hi, How can I help you?"
- Chat UI using Streamlit `st.chat_message` for role-based alignment
- Simple integration point for any backend/LLM via `agent_client.py`

## Quick start

Requirements

- Python 3.10+
- Windows (PowerShell examples below)
- Streamlit

Install and run:

```powershell
cd "c:\Abhinay\Code\Streamlit\ChatBot\Streamlit-ChatBot"
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt    # or: pip install streamlit requests python-dotenv
streamlit run app.py
```

Open the URL Streamlit prints (usually http://localhost:8501).

## Project layout

- `app.py` — Streamlit UI, quick prompts, chat flow
- `agent_client.py` — implements `get_agent_response(prompt: str) -> str` (your backend)
- `.gitignore` — ignores virtual env and caches
- `README.md` — this file

## agent_client example

Create `agent_client.py` and implement the function used by the UI:

```python
# agent_client.py
def get_agent_response(prompt: str) -> str:
    # Replace with your real backend call (API, LLM, etc.)
    return f"Placeholder reply for: {prompt}"
```

## Customization

- Update `quick_prompts` in `app.py` to change preset prompts.
- Adjust CSS blocks in `app.py` to refine look and feel.
- Add avatars or timestamps by extending the chat render loop.

## Troubleshooting

- Git commit error "Author identity unknown": set git identity:

```powershell
git config --global user.email "you@example.com"
git config --global user.name  "Your Name"
```

- If Streamlit chat APIs are missing, upgrade Streamlit:

```powershell
pip install --upgrade streamlit
```

## Contribute

Improve prompts, styling, or backend integration. Keep agent logic separate in `agent_client.py`.

## License

Add a LICENSE file as needed (e.g., MIT) before public distribution.
