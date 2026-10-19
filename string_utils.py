def check_string_length(text):
    if not isinstance(text, str):
        return "Invalid"
    if len(text) == 0:
        return "Empty"
    elif len(text) <= 5:
        return "Short"
    else:
        return "Long"