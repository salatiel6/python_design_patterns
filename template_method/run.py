import config_path # noqa

from src import CSVProcessor, PDFProcessor

data = ["AAA", 11]
csv_processor = CSVProcessor(data)
csv_processor.insert_data_in_doc()

data = ["BBB", 22]
pdf_processor = PDFProcessor(data)
pdf_processor.insert_data_in_doc()