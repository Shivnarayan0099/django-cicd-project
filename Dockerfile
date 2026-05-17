# 1. Base image standard Python environment choose kar rahe hain
FROM python:3.13-slim

# 2. Server ke andar environment variables set kar rahe hain
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 3. Container ke andar work directory (/app) create aur set kar rahe hain
WORKDIR /app

# 4. Local machine se requirements.txt ko container ke andar copy kar rahe hain
COPY requirements.txt /app/

# 5. Dependencies ko container ke andar install kar rahe hain
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# 6. Baki bacha hua pura code local machine se container mein copy kar rahe hain
COPY . /app/

# 7. Port 8000 ko open kar rahe hain jahan Django run hoga
EXPOSE 8000

# 8. Container start hote hi Django server chalane ki command
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]