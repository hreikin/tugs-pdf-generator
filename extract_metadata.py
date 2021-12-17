from PyPDF2 import PdfFileReader
import json

def get_metadata(input_file):

    # Opens (and closes because we are using "with".) provided input file in 
    # read mode.
    with open(input_file, "rb") as metadata_file:

        # Creates the file reader and gets the metadata and number of pages
        pdf_file_reader = PdfFileReader(metadata_file)
        metadata = pdf_file_reader.getDocumentInfo()
        number_of_pages = pdf_file_reader.getNumPages()
        pages_dict = {"/NumberOfPages": number_of_pages}

    # Processes the "/Keywords" metadata to strip the whitespace from within the 
    # string and then creates a list from the remaining items by using the comma 
    # as the delimiter.
    keyword_string = str()
    for k, v in metadata.items():
        if k == "/Keywords":
            keyword_string += v
        keyword_list = keyword_string.split(", ")

    # Creates the "processed_metadata" dictionary from items extracted from the 
    # PDF's metadata, then adds the "number_of_pages" dictionary and 
    # "keyword_list" list items as entries.
    processed_metadata = dict()
    processed_metadata["Author"] = metadata["/Author"]
    processed_metadata["Title"] = metadata["/Title"]
    processed_metadata["Subject"] = metadata["/Subject"]
    processed_metadata["NumberOfPages"] = pages_dict["/NumberOfPages"]
    processed_metadata["Keywords"] = keyword_list

    # Creates output file in write mode ("w"). Sorts the "key : value" pairs 
    # alphabetically and indents 4 spaces when exporting.
    with open(output_file, "w") as metadata_json_file:
        print("Exporting processed metadata to JSON file:", output_file)
        json.dump(processed_metadata, metadata_json_file, sort_keys = True, indent = 4)

if __name__ == "__main__":
    input_file = "meta_data_test.pdf"
    output_file = input_file.replace(".pdf", ".json")
    get_metadata(input_file)