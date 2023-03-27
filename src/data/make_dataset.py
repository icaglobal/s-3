def read_from_athena(path, query):
    """Fetch data from Athena tables.

        Using the library pyathena we set the user path to an s3 bucket.
        Then we pass the desired query returning a dataset.

        Parameters
        ----------

        path : string
            Path to Amazon s3 bucket
        quert : string
            An SQL query
            
        Returns
        -------

        df: dataframe
            A pandas dataframe containing the results of the query

        Example
        --------

        read_from_athena('s3://jonathan-oak/s3', '''select * from "fda-open-database"."recall" ''')

    """
    import pandas as pd
    from pyathena import connect

    conn=connect(s3_staging_dir=f'{path}', region_name='us-east-1')
    df = pd.read_sql(query,conn)
    
    return df
