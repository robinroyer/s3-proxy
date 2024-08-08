# Save this as mitm_script.py in the same directory as your Dockerfile
def request(flow):
    # Log request details
    print(f"Request: {flow.request.pretty_url}")

def response(flow):
    # Log response details
    print(f"Response: {flow.response.status_code} {flow.response.reason}")