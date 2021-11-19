import s3fs
from delta import *

_s3 = s3fs.S3FileSystem(s3_additional_kwargs={'ServerSideEncryption': 'AES256'})

output = _s3.ls("s3://your-bucket-name")
print(output)
