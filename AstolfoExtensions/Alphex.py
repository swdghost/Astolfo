import g4f
from g4f.Provider import (
    AItianhu,
    Acytoo,
    Aichat,
    Ails,
    Bard,
    Bing,
    ChatBase,
    ChatgptAi,
    H2o,
    HuggingChat,
    OpenAssistant,
    OpenaiChat,
    Raycast,
    Theb,
    Vercel,
    Vitalentum,
    Ylokh,
    You,
    Yqcloud,
)

def get_response(query):
    response = g4f.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": f" Answer this in short - Question : {query}"}],
    )
    return response

print(get_response("Hello, /Explain quantum mechanics"))