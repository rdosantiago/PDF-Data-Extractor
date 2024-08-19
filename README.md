# PDF-Data-Extractor
 Este repositório contém um script Python para extração de informações específicas de arquivos PDF e armazenamento desses dados em formatos de texto e Excel. A ferramenta lê o conteúdo de um arquivo PDF, salva o texto extraído em um arquivo .txt e utiliza expressões regulares para identificar e extrair dados-chave, como Número do Ofício, Número do Processo, Juiz Demandante, CPF/CNPJ, Data da Recepção e Número do Protocolo. Esses dados são então organizados e salvos em um arquivo Excel (.xlsx).

### Recursos:
- Leitura de conteúdo de arquivos PDF.
- Extração de informações específicas usando expressões regulares.
- Salvamento do conteúdo extraído em arquivos de texto (.txt) e Excel (.xlsx).

### Como Usar:
- Clone este repositório.
- Modifique os caminhos dos arquivos no script principal (main) para apontar para os seus arquivos PDF de entrada e arquivos de saída desejados.
- Execute o script para extrair e salvar os dados.

### Requisitos:
- Python 3.x
- PyPDF2
- Pandas
