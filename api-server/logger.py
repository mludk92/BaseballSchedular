log_store = []

def add_log(message: str):
    log_store.append(message)

def get_logs():
    return {"logs": log_store}
