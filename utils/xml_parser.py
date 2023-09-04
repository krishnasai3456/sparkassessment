import xml.etree.ElementTree as ET
import pandas as pd

def parse_and_flatten_xml(xml_string):
    root = ET.fromstring(xml_string)
    data = []

    for element in root.findall(".//record"):
        record = {}
        for child in element:
            record[child.tag] = child.text
        data.append(record)

    return data

def parse_and_flatten_xml_wrapper(sample_xml):
    flattened_data = parse_and_flatten_xml(sample_xml)

    df = pd.DataFrame(flattened_data)
    return df
