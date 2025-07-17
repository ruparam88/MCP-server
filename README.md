# 🧠 MCP Server – AI-Powered Medicine Recommendation API

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104.1-009688.svg)
![Hugging Face](https://img.shields.io/badge/🤗-Hugging%20Face-yellow.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)

A **Model Comparison Platform (MCP) server** that uses a pretrained Hugging Face model to compare user health queries with a structured medicine database and return the most relevant products. The API generates intelligent descriptions and product URLs using FastAPI.

---

## 🚀 Features

- 🔍 **Natural Language Processing**: Accepts queries like "headache and fever"
- 📊 **Smart Comparison**: Compares queries with medicine database from CSV
- 🧠 **AI-Powered Descriptions**: Uses Hugging Face models for custom descriptions
- 🌐 **RESTful API**: Clean FastAPI endpoints with automatic documentation
- 📱 **JSON Response**: Returns structured data including:
  - Medicine name
  - AI-generated description
  - Image URL
  - Product detail URL

---

## 🗂️ Project Structure

```
mcp-server/
├── app/
│   ├── __init__.py
│   ├── model_loader.py     # Load pretrained model
│   ├── database.py         # Load CSV into pandas
│   ├── comparator.py       # Query comparison logic
│   └── routes.py           # FastAPI endpoints
├── data/
│   └── products.csv        # CSV database
├── main.py                 # App entry point
├── requirements.txt        # Dependencies
├── README.md              # This file
└── .gitignore             # Git ignore file
```

---

## ⚙️ Setup Instructions

### Prerequisites

- Python 3.8 or higher
- pip package manager

### 1. Clone the repository

```bash
git clone https://github.com/ruparam88/MCP-server.git
cd MCP-server
```

### 2. Create virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Prepare your data

Place your `products.csv` file in the `data/` folder with the following structure:

```csv
name,composition,uses,side_effects,image_url
Crocin,Paracetamol 500mg,Fever and pain relief,Nausea in rare cases,https://example.com/crocin.jpg
Aspirin,Acetylsalicylic acid 325mg,Pain and inflammation,Stomach irritation,https://example.com/aspirin.jpg
```

### 5. Run the server

```bash
uvicorn main:app --reload
```

### 6. Access the API

- **Swagger UI**: http://127.0.0.1:8000/docs
- **ReDoc**: http://127.0.0.1:8000/redoc
- **API Endpoint**: http://127.0.0.1:8000/compare?q=your_query

---

## 🔌 API Endpoints

### `GET /compare?q=<query>`

Returns a list of matching medicines with AI-generated descriptions.

**Parameters:**
- `q` (string): Natural language health query

**Example Request:**
```http
GET /compare?q=headache and fever
```

**Example Response:**
```json
[
  {
    "name": "Crocin",
    "description": "Crocin is an effective pain reliever that helps alleviate headaches and reduce fever symptoms.",
    "image_url": "https://example.com/crocin.jpg",
    "url": "http://127.0.0.1:8000/product/Crocin"
  },
  {
    "name": "Aspirin",
    "description": "Aspirin provides relief from headaches and helps reduce fever through its anti-inflammatory properties.",
    "image_url": "https://example.com/aspirin.jpg",
    "url": "http://127.0.0.1:8000/product/Aspirin"
  }
]
```

### `GET /product/{product_name}`

Returns detailed information about a specific product.

**Parameters:**
- `product_name` (string): Name of the medicine

**Example Request:**
```http
GET /product/Crocin
```

**Example Response:**
```json
{
  "name": "Crocin",
  "composition": "Paracetamol 500mg",
  "uses": "Fever, pain relief, headache",
  "side_effects": "Nausea, dizziness (rare)",
  "image_url": "https://example.com/crocin.jpg"
}
```

---

## 🧠 AI Model Configuration

The system uses Hugging Face transformers for generating intelligent descriptions:

- **Default Model**: `gpt2` (lightweight and fast)
- **Alternative Models**: Any text-generation model from Hugging Face
- **Customization**: Modify `app/model_loader.py` to use your preferred model

### Supported Model Types:
- `text-generation` (GPT-2, GPT-3, etc.)
- `text2text-generation` (T5, BART, etc.)

---

## 🛠️ Development

### Running Tests

```bash
pytest tests/
```

### Code Formatting

```bash
black app/
flake8 app/
```

### Environment Variables

Create a `.env` file for configuration:

```env
MODEL_NAME=gpt2
MAX_LENGTH=100
TEMPERATURE=0.7
CSV_PATH=data/products.csv
```

---

## 📦 Dependencies

```txt
fastapi==0.104.1
uvicorn==0.24.0
pandas==2.1.3
transformers==4.35.2
torch==2.1.1
python-multipart==0.0.6
```

---

## 🚀 Deployment

### Local Development
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### Production (Docker)
```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Cloud Deployment Options
- **Heroku**: `git push heroku main`
- **Render**: Connect GitHub repository
- **AWS Lambda**: Use Mangum adapter
- **Google Cloud Run**: Deploy container

---

## 🔧 Future Improvements

- [ ] **Authentication**: JWT token-based user authentication
- [ ] **Frontend**: React/Vue.js web interface
- [ ] **Database**: PostgreSQL/MongoDB integration
- [ ] **Caching**: Redis for faster response times
- [ ] **Model Fine-tuning**: Domain-specific medical model
- [ ] **Analytics**: Usage tracking and metrics
- [ ] **Rate Limiting**: API usage limits
- [ ] **Logging**: Structured logging with ELK stack
- [ ] **Testing**: Comprehensive unit and integration tests

---

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines
- Follow PEP 8 style guide
- Write descriptive commit messages
- Add tests for new features
- Update documentation as needed

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- [Hugging Face](https://huggingface.co/) for transformer models
- [FastAPI](https://fastapi.tiangolo.com/) for the web framework
- [Pandas](https://pandas.pydata.org/) for data manipulation
- Contributors and the open-source community

---

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/yourusername/mcp-server/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/mcp-server/discussions)
- **Email**: your.email@example.com

---

## 🔗 Links

- **Live Demo**: [https://mcp-server-demo.herokuapp.com](https://mcp-server-demo.herokuapp.com)
- **API Documentation**: [https://mcp-server-demo.herokuapp.com/docs](https://mcp-server-demo.herokuapp.com/docs)
- **Hugging Face Model**: [https://huggingface.co/gpt2](https://huggingface.co/gpt2)

---

<div align="center">
  <strong>Made with ❤️ by [Your Name]</strong>
  <br>
  <sub>If this project helped you, please give it a ⭐!</sub>
</div>
