import logging
from box import Box

from utils.misc_utilities import timing, read_json

books1 = {"A Book You Read A Long Time Ago": {"title": "The Count of Monte Cristo", "pages": 782},
          "A Book Published in 2010": {"title": "The Way of Kings", "pages": 800},
          "A Book On your Shelf": {"title": "Fluent Python", "pages": 600}}

books2 = [{"desc": "A Book You Read A Long Time Ago",
           "name": "The Count of Monte Cristo",
           "pages": 782},
          {"desc": "A Book Published in 2010",
           "name": "The Way of Kings",
           "pages": 800},
          {"desc": "A Book On your Shelf",
           "name": "Fluent Python",
           "pages": 600}]

logger = logging.getLogger("boxes_demo_logger")
logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.DEBUG)

logger.info(f"Book's title from dictionary = {books1['A Book You Read A Long Time Ago']['title']}")

book_box1 = Box(books1)

logger.info(f"Book's title from Box = {book_box1.A_Book_You_Read_A_Long_Time_Ago.title}")

book_box2 = Box(books1, camel_killer_box=True)

logger.info(f"Book's title from Camel Case killed Box = {book_box2.a_book_you_read_a_long_time_ago.title}")

book_box3 = Box(books1, default_box=True, default_box_attr="NonExistent")

logger.info(f"Non existent Book's title from Box = {book_box3.momo}")

# Converting Box to YAML
book1_yml = book_box1.to_yaml()
book_box1.to_yaml("./outputs/books1.yaml")

# YAML to Box

book_box_from_yaml = Box.from_yaml(book1_yml)
logger.info(f"Box from YAML = {book_box_from_yaml}")


@timing
def read_Box(f_name):
    bx = Box.from_json(filename=f_name)


read_json("inputs/json_file.json")
read_Box("inputs/json_file.json")
