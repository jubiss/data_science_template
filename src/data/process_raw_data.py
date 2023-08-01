import sys,os
sys.path.append(os.getcwd())
import pandas as pd
from src.utils import utils

def process_raw_intern_data(save=False, file_name='intern_table'):
    table_path = r'data\raw\simulated_listings1.csv'
    internal_processed_table = pd.read_csv(table_path)
    if save:
        utils.save_csv(internal_processed_table, filepath_name=f'data/processed/{file_name}.csv', save=save)
    return internal_processed_table

def process_raw_extern_data(save=False, file_name='intern_table'):
    table_path = r'data\external\enderecos_problema.csv'
    internal_processed_table = pd.read_csv(table_path)
    if save:
        utils.save_csv(internal_processed_table, filepath_name=f'data/processed/{file_name}.csv', save=save)
    return internal_processed_table

def merge_internal_external_data(intern_data, external_data, save=False, file_name='final_table'):

    int_ext_data = intern_data.merge(external_data, on=['latitude', 'longitude'], how='left')
    if save:
        utils.save_csv(int_ext_data, filepath_name=f'data/processed/{file_name}.csv', save=save)
    return int_ext_data

if __name__ == '__main__':
    intern_data = process_raw_intern_data(save=False, file_name='internal_table')
    external_data = process_raw_extern_data(save=False, file_name='external_table')
    merge_internal_external_data(intern_data, external_data, save=True, file_name='listings_with_address')