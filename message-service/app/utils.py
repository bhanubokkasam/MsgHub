def format_error(message):
    return {"error": message}, 400

def handle_404_error(e):
    return format_error("Resource not found")

def handle_500_error(e):
    return format_error("Internal server error")
