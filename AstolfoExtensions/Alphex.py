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
        model=g4f.models.default,
        messages=[{"role": "user", "content": f"Refer to Youself as an imaginary character named Astolfo.  Answer this in short - Question : {query}"}],
    )
    return response