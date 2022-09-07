from .template import Template


class PDFProcessor(Template):
    def insert_data_in_doc(self):
        print("Connecting from PDF file")
        print(self.data)
        print("Saving Data")