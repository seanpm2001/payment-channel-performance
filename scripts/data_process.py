# this script is used to extract gas price and related waiting time
import pandas as pd
import re
import json
import unicodecsv as csv

# remove substrings before and after two characters
# exmaple:
# input: '12@[123]57'. '[',']'
# output: '[123]'
def remove_redundant_characters(str, char1, char2):
    left_index = str.find(char1)
    right_index = str.find(char2)
    result = str[left_index: (right_index +1)]
    return result

# extract gas and waiting time information from raw data
# input: str by reading csv files
# output: json format data
def extract_data(str):
    # extract data as string from csv file
    result = re.search('var _data = (.*) var _sliderData = ', str)
    result = result.group(0)  # type: object
    result = remove_redundant_characters(result, '[', ']')

    # extract data as json from string
    result = json.loads(result)
    return result


# write data into file
def write_to_file(file,fieldnames, data):
    with open(file, 'ab')as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames,quoting=csv.QUOTE_ALL)
        writer.writeheader()
        try:
            for item in data:
                assert isinstance(item, object)
                writer.writerow(item)
        except Exception as e :
            print("error when writing data to file")
            print(e.message)
    csvfile.close()
#####################################################################


file = 'data/db.json'
with open(file,'r') as f:
        data = json.load(f)
        print(len(data))
