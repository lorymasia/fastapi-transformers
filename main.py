from transformers import pipeline
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

#sentiment-analysis -> analisi del sentimento di un testo
#summarization -> permette di fare il riassunto di un testo
#text-generation -> genera del testo
#translation -> traduzioni da una lingua ad un altra
#zero-shot-classification -> consente di classificare un testo in categorie 
        #definite dall'utente senza che il modello sia stato addestrato 
        #esplicitamente su quelle categorie.

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def form(request: Request):
    return templates.TemplateResponse(request=request, name="form.html")

@app.get("/riassunto", response_class=HTMLResponse)
def riassunto(request: Request, summary):
    classifier = pipeline("summarization")
    text = classifier(summary)
    return templates.TemplateResponse(request=request, name="riassunto.html", context={"summary": text[0]["summary_text"]})


