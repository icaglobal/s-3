import sys
sys.path.insert(0, '../')

from data.make_dataset import read_from_athena

query = ''' 
        SELECT 
            event_date_initiated,
            event_date_posted,
            product_code,
            code_info,
            product_quantity,
            k_numbers,
            firm_fei_number,
            product_description,
            root_cause_description,
            openfda,
            event_date_terminated,
            product_res_number,
            res_event_number
        FROM 
            "fda-open-database"."recall"
        LIMIT 10
        '''

path = 's3://jonathan-oak/s3'

recall_df = read_from_athena(path, query)