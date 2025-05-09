# Smart PDF Chat

A modern, ChatGPT-like interface for interacting with PDF documents using AI. This application allows users to upload PDF files and ask questions about their content, receiving AI-powered responses.

## ✨ Features

- 📄 **PDF Document Upload**: Upload and process PDF files seamlessly
- 💬 **Modern ChatGPT-like Interface**: Clean and intuitive user experience
- 🤖 **AI-Powered Question Answering**: Get intelligent responses about your PDF content
- 🎨 **Sleek Dark Theme Design**: Modern and eye-friendly interface
- 📱 **Responsive Layout**: Works perfectly on all devices
- ⚡ **Real-time Chat Experience**: Smooth and responsive interactions

## 🛠️ Tech Stack

### Frontend
- HTML5
- TailwindCSS
- JavaScript
- SweetAlert2 for Notifications

### Backend
- Python (FastAPI)
- Pinecone Vector Database
- Google Generative AI
- Google Cloud Storage (GCS)

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- uv package manager
- Modern web browser

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Srinath991/Smart-PDF-Chat.git
   cd Smart-PDF-Chat
   ```

2. **Install Python dependencies**
   ```bash
   uv sync
   ```

3. **Set up environment variables**

   Create a `.env` file with the following environment variables:

   To set up the required credentials:

   **Google Cloud Setup:**
   1. Go to [Google Cloud Console](https://console.cloud.google.com)
   2. Create a new project or select existing one
   3. Enable Vertex AI API and Cloud Storage API
   4. Create a service account and download JSON key
   5. Copy the values from your JSON key file

   **Pinecone Setup:**
   1. Sign up at [Pinecone](https://www.pinecone.io)
   2. Create a new project
   3. Create an index with dimensions=768 and metric=cosine
   4. Copy the values from your Pinecone console

   **Google Gemini Setup:**
   1. Go to Google AI Studio
   2. Create an API key

   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

4. **Start the application**
   ```bash
   uv run app/main.py
   ```

5. **Access the application**
   Open your browser and navigate to:
   ```
   http://localhost:8000
   ```

## 📖 Usage Guide

### Uploading a PDF
1. Click the file input or drag and drop a PDF file
2. Wait for the upload to complete
3. You'll receive a success notification when the upload is finished

### Asking Questions
1. Type your question in the input box at the bottom
2. Press Enter or click the "Ask" button
3. View the AI-generated response in the chat interface

### Chat Interface
- User messages appear on the right
- AI responses appear on the left
- Scroll through chat history as needed
- Clear and modern message formatting

## 📄 License

This project is licensed under the MIT License
