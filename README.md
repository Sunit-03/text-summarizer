# 🦙 LLaMA Text Summarizer

A simple text summarization app using the **Gemma:2b model via Ollama**, powered by **FastAPI** (backend) and **Streamlit** (frontend). Run everything locally and summarize large chunks of text in seconds.

---

## 🔍 Overview

- 🔁 Summarize long text using LLaMA locally  
- ⚡ FastAPI backend to interact with the model  
- 🎨 Streamlit frontend for user interaction  
- 🧪 LLM runs locally using [Ollama](https://ollama.com)

---

## 🛠️ Tech Stack

- 🦙 **Gemma:2b** (via Ollama)  
- 🚀 **FastAPI** – RESTful backend  
- 🖥 **Streamlit** – Interactive frontend UI  
- 🗂 **Git/GitHub** – Version control & collaboration


---
# 📁 Project Structure
```
text-summarizer-llama/
├── backend/
│   └── main.py
├── frontend/
│   └── app.py
├── requirements.txt
├── README.md
└── LICENSE
```

---

## ⚙️ Setup Instructions

## Step1: 📥 Clone the Repo

To get started with the project, first clone the repository:

```bash
git clone https://github.com/Hardik-Sankhla/Text-Summarizer-Using-Llama-Ollama.git
cd Text-Summarizer-Using-Llama-Ollama
```

### Step 2: Environment Setup

```bash
$ python -m venv venv

# On Windows
$ venv\Scripts\activate

# On macOS/Linux
$ source venv/bin/activate
```

#### Install dependencies:

```bash
$ pip install -r requirements.txt
```

### Step 3: Install & Run Ollama

Download Ollama and install it.

#### Start Ollama and pull the LLaMA model:

```bash
$ ollama pull llama2
```

#### Run the App
Start the backend using FastAPI:

```bash
$ uvicorn backend.main:app --reload
```

Start the frontend using Streamlit:

```bash
$ streamlit run frontend/app.py
```

#### Then open the app in your browser, enter any text, and get a clean summary powered by LLaMA.


---
## 📃 License

This project is licensed under the [MIT License](LICENSE) © 2025 Sunit Mohan.
Feel free to use, modify, and share with attribution.

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you’d like to change.

---

## 🌐 Author
#### Sunit Mohan
