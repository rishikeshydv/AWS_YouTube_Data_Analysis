import os
import awswrangler as wr
import urllib.parse
import pandas as pd

os_input_s3_cleansed_layer = os.environ['s3_cleansed_layer']
os_input_glue_catalog_db_name = os.environ['glue_catalog_db_name']
os_input_glue_catalog_table_name = os.environ['glue_catalog_table_name']
os_input_write_data_operation = os.environ['write_data_operation']

def data_format(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')

    try:
        df_all = wr.s3.read_json('s3://{}/{}'.format(bucket,key))
        item_column = pd.json_normalize(df_all['items'])
        write_to_s3 = wr.s3.to_parquet(
            df = item_column,
            path = os_input_s3_cleansed_layer,
            dataset = True,
            database = os_input_glue_catalog_db_name,
            table = os_input_glue_catalog_table_name,
            mode = os_input_write_data_operation
                )

        return write_to_s3

    except Exception as e:
        print(e)
        raise e



