import PyPDF2
# En terminal: pip install PyPDF2
import json


def load_pdf(path_file):
    with open(path_file, 'rb') as book:
        pdf = PyPDF2.PdfReader(book)
        num_pages = len(pdf.pages)
        
        for page in range(num_pages):
            result = pdf.pages[page]
            print(result.extract_text())
            

def load_txt(path_file):
    with open(path_file, 'r') as file:
        data = file.readlines()
        print(data)
    
        
def write_txt(path_file, data):
    with open(path_file, 'w', encoding='utf-8') as file:
        file.write(data)
        
def load_json(path_file):
    with open(path_file, 'r') as file:
        return json.load(file)
        
def write_json(path_file, data):
    with open(path_file, 'w', encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
    