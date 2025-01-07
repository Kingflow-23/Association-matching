import os
from PyPDF2 import PdfReader
import pandas as pd

df = pd.DataFrame()

name = ["Abalone", "Carasso", "UEM", "Michelin"]

df["Fondations"] = name
df["Textes"] = [None] * len(name)

# Chemin du répertoire contenant les CV (fichiers PDF)
fondations_folder = r"Pdfs"
# Liste tous les fichiers PDF dans le dossier
pdf_files = [
    os.path.join(fondations_folder, file)
    for file in os.listdir(fondations_folder)
    if file.endswith(".pdf")
]


# Fonction pour extraire le texte d'un fichier PDF
def extract_text_from_pdf(pdf_file_path):
    text = ""
    pdf_reader = PdfReader(pdf_file_path)
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text


# Parcours de chaque fichier PDF et extraction du texte
# Enumerate est une fonction quifait une liste de
for i, pdf_file_path in enumerate(pdf_files):
    cv_text = extract_text_from_pdf(pdf_file_path)
    df.at[i, "Textes"] = cv_text

print(df)