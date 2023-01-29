import emoji

def emoji_remover(text):
    return emoji.replace_emoji(text, "")