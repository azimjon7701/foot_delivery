def format_time(seconds):
    minutes, seconds = divmod(seconds, 60)
    time_string = ""
    if minutes:
        time_string += f"{minutes} minutes "
    if seconds:
        time_string += f"{seconds} seconds"
    return time_string.strip()