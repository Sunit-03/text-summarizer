from fastapi import FastAPI, Form
import requests

app = FastAPI()

@app.post("/summarize/")
def summarize(text: str = Form(...)):
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "gemma:2b",
                "prompt": f"Summarize this:\n\n{text}",
                "stream": False
            }
        )
        if response.status_code != 200:
            return {"summary": f"Error: Ollama returned status {response.status_code}"}
        
        result = response.json()
        return {"summary": result.get("response", "No summary in response")}
    except Exception as e:
        return {"summary": f"Backend error: {str(e)}"}
