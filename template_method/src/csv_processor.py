from .template import Template


class CSVProcessor(Template):
    def insert_data_in_doc(self):
        print("Connecting from CSV file")
        print(self.data)
        print("Saving Data")
