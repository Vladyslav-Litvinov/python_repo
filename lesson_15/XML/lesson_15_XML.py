import xml.etree.ElementTree as ET
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger("xml_search")

def find_timing_exbytes_incoming(xml_file, group_number):
    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()

        for group in root.findall('group'):
            number = group.find('number')
            if number is not None and number.text == str(group_number):
                timing_exbytes = group.find('timingExbytes')
                if timing_exbytes is not None:
                    micro = timing_exbytes.find('micro').text if timing_exbytes.find('micro') is not None else "N/A"
                    bbo = timing_exbytes.find('bbo').text if timing_exbytes.find('bbo') is not None else "N/A"
                    incoming = timing_exbytes.find('incoming').text if timing_exbytes.find(
                        'incoming') is not None else "N/A"

                    logger.info(f"Found in {xml_file}: micro={micro}, bbo={bbo}, incoming={incoming}")
                    return micro, bbo, incoming
        logger.info(f"Value not found in {xml_file} for group/number {group_number}")
        return None
    except ET.ParseError as e:
        logger.error(f"Error parsing {xml_file}: {e}")
        return None

current_directory = Path(__file__).parent
groups_xml_path = current_directory / 'groups.xml'
group_number_to_search = 5 # вводимо потрібне нам значення группи\номера
find_timing_exbytes_incoming(groups_xml_path, group_number_to_search)
