import os
import numpy as np
import pandas as pd

def check_obsolete(path):
    """
    A function to check if a product is obsolete
    :param path: The complete path to the csv file
    :return: dataframe containing a new column stating if the product is expired or not
    """
    df = pd.read_csv(path)
    df['obsolete']= df['date'] < '2021-01-01'

    return df

def convert_to_json(df, file_name, file_path):
    """
    A function to convert a dataframe to json
    :param df: The dataframe to be converted
    :param file_name: The file name to save the json with
    :param file_path: The file path to save the json file in
    :return: None
    """
    df.to_json(os.path.join(file_path,file_name))



