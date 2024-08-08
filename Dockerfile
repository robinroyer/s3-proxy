# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Install mitmproxy
RUN pip install mitmproxy

# Copy the mitmproxy script into the container
COPY mitm_script.py /app/mitm_script.py

# Expose the mitmproxy ports
EXPOSE 8080 8081

# Start mitmproxy in transparent mode
ENTRYPOINT ["mitmdump", "--mode", "regular", "-s", "/app/mitm_script.py"]

# You can also use mitmproxy directly for a web interface:
# ENTRYPOINT ["mitmproxy", "--mode", "regular", "-s", "/app/mitm_script.py"]