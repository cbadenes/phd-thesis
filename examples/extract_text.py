import fitz  # this is pymupdf
import csv
import os

def extract_information(pdf_path):
    with fitz.open(pdf_path) as doc:
        data = {}
        text = ""
        data['title']= doc.metadata['title']        
        
        for num_page in range(doc.pageCount-1):
            page = doc.loadPage(num_page)
            text += page.getText().replace("\n"," ")
        data['text'] = text
        return data
        

if __name__ == '__main__':
    with open('corpus.csv', mode='w') as output_file:
        csv_writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        
        for root, dirs, files in os.walk(os.path.abspath("../../../publications/contribution/")):
            for file in files:
                if (file.endswith(".pdf")):
                    pdf_path = os.path.join(root, file)
                    print(pdf_path)
                    pdf_data = extract_information(pdf_path)
                    csv_writer.writerow([pdf_data['title'], pdf_data['text']])
    
