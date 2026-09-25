from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

from agent_Parser import agent_parser
from is_valid import is_valid_json, validate_schema
from PDF2Txt import PyMyPDF


app = FastAPI()


# Autoriser le frontend à appeler l'API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/upload")
async def upload_cv(
    cv: UploadFile = File(...),
    linkedin: str = Form(""),
    github: str = Form(""),
    website: str = Form("")
):
    # Lire le fichier
    file_bytes = await cv.read()

    # Extraire le texte du CV
    cv_text = PyMyPDF(file_bytes)
    output = agent_parser(cv_text)
    output_json = is_valid_json(output)
    if not validate_schema(output_json):
        return {"error": "Schema invalide"}

    output_json["linkedin"]= linkedin
    output_json["github"]=github
    output_json["website"]: website
    return {
        "cv": output_json
    }


@app.get("/upload.html")
def page():
    return FileResponse(
        "Template/Abdessamad AMTOUG — Ajouter CV & liens.html"
    )


@app.get("/Portfolio.html")
def page2():
    return FileResponse(
        "Template/Abdessamad AMTOUG — Portfolio.html"
    )