# Use the latest version of Ubuntu as the base image
FROM ubuntu:latest

# Update package lists and install required packages
RUN apt-get update && apt-get install -y \
    tar \
    wget \
    python3 \
    gcc \
    g++ \
    git \
    && rm -rf /var/lib/apt/lists/*

# Set the default working directory
WORKDIR /workspace

# Download CodeQL bundle using wget
RUN wget https://github.com/github/codeql-action/releases/download/codeql-bundle-v2.17.0/codeql-bundle-linux64.tar.gz \
    && tar -xzf codeql-bundle-linux64.tar.gz -C /workspace \
    && rm codeql-bundle-linux64.tar.gz

# Set environment variables for CodeQL
ENV PATH="/workspace/codeql:${PATH}"

# Copy run.sh and src directory into the workspace
COPY run.sh /workspace/
COPY src /workspace/src/

# Make run.sh executable
RUN chmod +x run.sh

# Execute the run.sh script when the container starts
CMD ["./run.sh"]

