max_length = 140
def truncated_text(text: str):
    if len(text) <= 140:
        return text

    return text[:(max_length - 3)] + "文字数"