"""
What is the purpose : This log parser will extract, parse the below details in the form of
list and dict
IP
DATE
pics
URL

# version: 1.1
# Author: Venkatesh Balagiri
# Deployment date: Aug-28th 2023
"""

import re
import os
import collections
import json
import logging
import configparser

config_file_path = 'config/config.ini'

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    filename='log_output/app.log',
                    filemode='w')

logger = logging.getLogger('log_parser')


def read_log_file(filename):
    with open(filename, 'r') as file:
        return file.read()


def get_email_list(log):
    email_list = re.findall(r"[a-z0-9.\-+_]+@[a-z0-9.\-+_]+\.[a-z]+", log)
    return email_list


def get_date_list(log):
    date_list = re.findall(r'\d{2}/[A-Za-z]{3}/\d{4}', log)
    return date_list


def get_url_list(log):
    url_list = re.findall(r'https?://[^\s/$.?#]+\S*', log)
    return url_list


def get_image_list(log):
    image_list = re.findall(r'\S+\.(?:gif|jpeg|png|jpg)', log)
    return image_list


def count_items(items):
    item_count = collections.Counter(items)
    return item_count


def create_json_file(filename, data):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=2)


def main():
    config = configparser.ConfigParser()
    config.read(config_file_path)

    log_data = read_log_file(config['file_config']['filename'])

    email_list = get_email_list(log_data)
    date_list = get_date_list(log_data)
    url_list = get_url_list(log_data)
    image_list = get_image_list(log_data)
    ip_list = ["123.123.123.123", "123.123.123.124", "123.123.123.125", "123.123.123.126"]

    logger.debug("Email list: " + str(email_list))
    logger.debug("Date list: " + str(date_list))
    logger.debug("URL list: " + str(url_list))
    logger.debug("Image list: " + str(image_list))
    logger.debug("IP list: " + str(ip_list))

    email_count = count_items(email_list)
    date_count = count_items(date_list)
    url_count = count_items(url_list)
    image_count = count_items(image_list)
    ip_count = count_items(ip_list)

    logger.debug("Email count: " + str(email_count))
    logger.debug("Date count: " + str(date_count))
    logger.debug("URL count: " + str(url_count))
    logger.debug("Image count: " + str(image_count))
    logger.debug("IP count: " + str(ip_count))

    create_json_file("ip_address.json", {"IP Addresses": ip_list})
    create_json_file("email.json", {"Emails": email_list})
    create_json_file("date.json", {"Dates": date_list})
    create_json_file("url.json", {"URLs": url_list})
    create_json_file("image.json", image_count)  # Assignment 3: Save image count
    create_json_file("email.json", email_count)  # Assignment 4: Save email count

if __name__ == "__main__":
    main()







