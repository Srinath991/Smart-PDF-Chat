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
  - Vector Database for PDF Storage
  - AI/LLM Integration

## Getting Started

### Prerequisites

- Python 3.8+
- Modern web browser

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/smart-pdf-chat.git
   cd smart-pdf-chat
   ```

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

4. Start the application:
   ```bash
   python app/main.py
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
   - User messages appear on the right
   - AI responses appear on the left
   - Scroll through chat history as needed

## Development

### Project Structure

```
smart-pdf-chat/
├── app/
│   ├── static/
│   │   └── main.js
│   ├── templates/
│   │   └── index.html
│   └── main.py
├── requirements.txt
└── README.md
```

### Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- ChatGPT for UI inspiration
- TailwindCSS for the styling framework
- SweetAlert2 for beautiful notifications
