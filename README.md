# Smart PDF Chat

A modern, ChatGPT-like interface for interacting with PDF documents using AI. This application allows users to upload PDF files and ask questions about their content, receiving AI-powered responses.

## Features

- 📄 PDF Document Upload
- 💬 Modern ChatGPT-like Interface
- 🤖 AI-Powered Question Answering
- 🎨 Sleek Dark Theme Design
- 📱 Responsive Layout
- ⚡ Real-time Chat Experience

## Tech Stack

- **Frontend**:
  - HTML5
  - TailwindCSS
  - JavaScript 
  - SweetAlert2 for Notifications

- **Backend**:
  - Python (FastAPI)
  - Pinecone Vector Database 
  - google generative AI and google cloud storage(GCS)
  - AI/LLM Integration

## Getting Started

### Prerequisites

- Python 3.8+
- uv package manager
- Modern web browser

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Srinath991/Smart-PDF-Chat.git
   cd Smart-PDF-Chat
   ```

2. Install Python dependencies:
   ```bash
  uv sync
   ```

3. Set up environment variables:
   Create a `.env` file with the following environment variables:

   ```env
   # Google Cloud Credentials
   # 1. Go to Google Cloud Console (https://console.cloud.google.com)
   # 2. Create a new project or select existing one
   # 3. Enable Vertex AI API and Cloud Storage API
   # 4. Create a service account and download JSON key
   # 5. Copy these values from your JSON key file

   # Pinecone Credentials
   # 1. Sign up at Pinecone 
   # 2. Create a new project
   # 3. Create an index with dimensions=768 and metric=cosine 
   # 4. Copy these values from your Pinecone console


   # Google Gemini API Key
   # 1. Go to Google AI Studio 
   # 2. Create an API key
   ```

   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

4. Start the application:
   ```bash
   uv run app/main.py
   ```

5. Open your browser and navigate to:
   ```
   http://localhost:8000
   ```

## Usage

1. **Upload a PDF**:
   - Click the file input or drag and drop a PDF file
   - Wait for the upload to complete

2. **Ask Questions**:
   - Type your question in the input box at the bottom
   - Press Enter or click the "Ask" button
   - View the AI-generated response

3. **Chat Interface**:
   - Messages are displayed in a modern chat interface
   - User messages 
   - AI responses 
   - Scroll through chat history as needed


### Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License
