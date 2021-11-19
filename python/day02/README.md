# Day 2 - Parquet Format

Write, read and analyze Parquet files locally.

### Write Parquet

Writes from pandas to a local parquet file.

```python
# 01_write_parquet.py

import numpy as np
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

df = pd.DataFrame({
    'one': [-1, np.nan, 2.5],
    'two': ['foo', 'bar', 'baz'],
    'three': [True, False, True]
}, index=list('abc'))

table = pa.Table.from_pandas(df)
pq.write_table(table, 'example.parquet')
```

### Read Parquet

Reads from a local parquet file and loads data in pandas.

```python
# 02_read_parquet.py

import numpy as np
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

table = pq.read_table('example.parquet')

df = table.to_pandas()
print(df)
```

### Filter data

To filter the data read from the parquet file, below are some examples (the file is in Jupyter Notebook format to visualize the output):

```python
# 03_filter_parquet.ipynb

import pandas as pd
parquet_file = "example.parquet"
df = pd.read_parquet(parquet_file, engine='pyarrow')

# show the first lines of a table
df.head()

# show selected column(s) of the table
df[["one", "two"]].head()

# filter rows by value
df[df["two"]=="foo"].head()

# filter rows by value
df[df["three"]==True].head()

# filter rows by value
df[df["one"]>0].head()
```