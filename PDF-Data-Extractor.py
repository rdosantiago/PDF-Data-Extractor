import os
import re
import PyPDF2
import pandas as pd

class PDFHandler:
    def __init__(self, pdf_path, output_path_txt, output_path_excel):
        self.pdf_path = pdf_path
        self.output_path_txt = output_path_txt
        self.output_path_excel = output_path_excel

    def read_pdf(self):
        with open(self.pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            content = ""
            for page_number in range(len(reader.pages)):
                page = reader.pages[page_number]
                content += page.extract_text()
            return content

    def save_to_txt(self, content):
        with open(self.output_path_txt, 'w', encoding='utf-8') as file:
            file.write(content)

    def extract_data(self, text):
        patterns = {
            "Número do Ofício": r"Número do protocolo:\s*(\d+)",
            "Número do Processo": r"^(?:.*\n){5}([0-9\-.]{25})",
            "Juiz Demandante": r"^(?:.*\n){6}(.*?)\s+protocolado",
            "CPF/CNPJ": r"^(?:.*\n){21}(\d+)\s*:",
            "Data da Recepção": r"^(?:.*\n){3}(\d{2}/\d{2}/\d{4})",
            "Número do Protocolo": r"Número do protocolo:\s*(\d+)"
        }

        data = {}
        for key, pattern in patterns.items():
            match = re.search(pattern, text)
            if match:
                data[key] = match.group(1)
        return data

    def save_to_excel(self, data):
        df = pd.DataFrame([data])
        df.to_excel(self.output_path_excel, index=False)
        print(f"As informações foram salvas no arquivo {self.output_path_excel}")

def main():
    pdf_path = r'C:\Users\rdosa\source\repos\PythonApplication3\Bloqueio-Sisbajud.pdf'
    output_path_txt = r'C:\Users\rdosa\source\repos\PythonApplication3\resultado.txt'
    output_path_excel = r'C:\Users\rdosa\source\repos\PythonApplication3\informacoes_extraidas.xlsx'
    
    pdf_handler = PDFHandler(pdf_path, output_path_txt, output_path_excel)
    
    # Leia o PDF e salve o conteúdo em um arquivo de texto
    content = pdf_handler.read_pdf()
    pdf_handler.save_to_txt(content)
    
    # Extraia os dados do arquivo de texto e salve em um arquivo Excel
    extracted_data = pdf_handler.extract_data(content)
    pdf_handler.save_to_excel(extracted_data)

if __name__ == "__main__":
    main()
