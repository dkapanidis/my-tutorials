import numpy as np
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

table = pq.read_table('example.parquet')

df = table.to_pandas()
print(df)
