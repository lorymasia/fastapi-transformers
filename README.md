# ✨ Text Summarization Web App

Questa è una semplice web app realizzata con **FastAPI** che utilizza il modello di Hugging Face `transformers` per eseguire il **riassunto di un testo** (text summarization).

## 🚀 Funzionalità

- Interfaccia web per inserire un testo.
- Riassunto automatico del testo grazie al modello `summarization` di Hugging Face.
- Rendering delle pagine HTML tramite Jinja2.

## 🛠️ Tecnologie utilizzate

- [FastAPI](https://fastapi.tiangolo.com/) – Web framework per API veloci ed efficienti.
- [Transformers](https://huggingface.co/docs/transformers/index) – Libreria di modelli pre-addestrati NLP.
- [Jinja2](https://jinja.palletsprojects.com/) – Template engine per il rendering HTML.
- [Hugging Face Pipeline](https://huggingface.co/docs/transformers/main_classes/pipelines) – API semplificata per usare i modelli NLP.

## 📦 Requisiti

Assicurati di avere Python 3.8 o superiore. Installa le dipendenze con:

pip install -r requirements.txt

▶️ Come avviare l'app
Per avviare il server FastAPI in locale:

uvicorn main:app --reload
L'app sarà disponibile su http://localhost:8000

## 📂 Struttura del progetto
.
├── main.py # Applicazione principale FastAPI con routing e logica NLP
├── requirements.txt # File delle dipendenze del progetto
└── templates/ # Cartella dei template HTML
├── form.html # Pagina iniziale con il form per inserire il testo
└── riassunto.html # Pagina che mostra il risultato del riassunto
    
💡 Esempi futuri
Nel codice sono presenti commenti che anticipano l'integrazione di altre funzionalità tramite Hugging Face, come:

Analisi del sentimento

Generazione di testo

Traduzioni

Classificazione zero-shot

📖 Licenza
Questo progetto è open-source e disponibile sotto licenza MIT.
