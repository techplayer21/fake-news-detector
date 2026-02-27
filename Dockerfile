# Step 1: Use a lightweight Python base image
FROM python:3.9-slim

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy all files from your current folder to the container
COPY . /app

# Step 4: Install the necessary Python libraries
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Expose the port Streamlit runs on
EXPOSE 8501

# Step 6: Start the Streamlit app when the container launches
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]