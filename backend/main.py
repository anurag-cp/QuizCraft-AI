from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import pdfplumber
import re
import io

app = FastAPI()

# Enable CORS so the React frontend can communicate with the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/upload-pdf")
async def upload_pdf(file: UploadFile = File(...)):
    if not file.filename.endswith('.pdf'):
        raise HTTPException(status_code=400, detail="Only PDF files are allowed")
    
    try:
        content = await file.read()
        text = ""
        
        # Parse the PDF from memory
        with pdfplumber.open(io.BytesIO(content)) as pdf:
            for page in pdf.pages:
                extracted = page.extract_text()
                if extracted:
                    text += extracted + "\n"
        
        # Regex to match standard quiz format
        pattern = r"(?:Question\s*\d+:?|^\d+\.)\s*(.*?)\n(A\).*?)\n(B\).*?)\n(C\).*?)\n(D\).*?)\nAnswer:\s*([A-D])"
        matches = re.findall(pattern, text, re.DOTALL | re.MULTILINE)
        
        quiz_data = []
        for match in matches:
            options = [match[1].strip(), match[2].strip(), match[3].strip(), match[4].strip()]
            correct_letter = match[5].strip()
            
            # Find the full string of the correct option
            correct_answer = next((opt for opt in options if opt.startswith(correct_letter)), "")
            
            quiz_data.append({
                "question": match[0].strip(),
                "options": options,
                "correct_answer": correct_answer
            })
            
        if not quiz_data:
            raise HTTPException(status_code=400, detail="No questions found. Check PDF formatting.")
            
        return {"quiz_data": quiz_data}
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))