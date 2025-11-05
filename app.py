import streamlit as st
from agent_client import get_agent_response

st.set_page_config(page_title="APISM Assist", page_icon="🤖")

st.title("🤖 API Subscription Manager Assist")

# Initialize chat session with a default assistant greeting
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hi, How can I help you?"}
    ]

# Predefined quick prompts (shown statically at the top)
quick_prompts = [
    "List all APIs Published on Kong Developer Portal",
    "List routes of API AppCI 'EII'",
    "List all subscriptions for API Provider appCI 'EII'",
    "List all subscriptions for Consumer Application appCI 'EIF'",
    "List all consumers applications registered on Entra ID for consumer appCI 'ESD'",
    "Get Admins of application appCI 'ESD'",
    "Summarize the details of API Provider 'EII'",
    "Retrieve OpenAPI Spec or Swagger for API appCI 'EII'"
]

# Top: Quick prompts (compact vertical list, professional styling)
st.subheader("Quick prompts")
st.markdown(
    """
    <style>
    /* compact professional prompt list */
    .stButton>button {
        width: 100%;
        text-align: left;
        padding: 10px 14px;
        font-size: 13px;
        border-radius: 8px;
        background-color: #ffffff;
        color: #0f1724;
        border: 1px solid #e6e9ee;
        box-shadow: 0 1px 0 rgba(15,23,36,0.03);
        margin-bottom: 8px;
    }
    .stButton>button:hover { background-color: #f6f8ff; }
    .prompt-sub { display:block; color:#6b7280; font-size:11px; margin-top:4px; }
    </style>
    """,
    unsafe_allow_html=True,
)

# Render quick prompts as a vertical list (small/compact)
for i, prompt in enumerate(quick_prompts):
    # prepend a subtle icon to improve visual hierarchy
    label = f"💡  {prompt}"
    if st.button(label, key=f"quick_{i}"):
        # handle selection just like user input
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.spinner("APISM Assist is typing..."):
            response = get_agent_response(prompt)
        st.session_state.messages.append({"role": "assistant", "content": response})

st.markdown("---")

# Middle: Chat history (messages)
st.subheader("Chat")
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Bottom: Chat input (always at page bottom in script order)
user_input = st.chat_input("Ask your queries...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.spinner("APISM Assist is typing..."):
        response = get_agent_response(user_input)
    st.session_state.messages.append({"role": "assistant", "content": response})