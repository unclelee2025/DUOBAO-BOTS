def is_private(chat_type: str) -> bool:
    return chat_type == "private"

def mask(text: str, head=3, tail=3):
    if not text or len(text) <= head + tail:
        return text
    return f"{text[:head]}...{text[-tail:]}"
