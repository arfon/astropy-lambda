## Astropy and Lambda

This repo is a WIP but the general idea is to get Astropy running on [AWS Lambda](https://aws.amazon.com/lambda/).

This repository is an example of a directory that can be zipped up and deployed to Lambda.

### Built from

- https://github.com/vitolimandibhrata/aws-lambda-numpy
- https://stackoverflow.com/questions/34749806/using-moviepy-scipy-and-numpy-in-amazon-lambda
- https://docs.aws.amazon.com/lambda/latest/dg/with-s3-example-deployment-pkg.html#with-s3-example-deployment-pkg-python

### What the actual code looks like

Once the dependencies are installed (e.g. `numpy` and `astropy`) you need to defined the function for Lambda to execute. In this case we have a file named `process.py` and a `handler` function. We configure Lambda to execute `process.handler`

Currently we have the FITS file location hard-coded into the processing code but this could be dynamically passed.

#### What this code does

The following code downloads a FITS file from the [Hubble Legacy Archive](https://hla.stsci.edu) and inspects the contents of the file using `astropy.io.fits`

```python
import os
import subprocess
import uuid

libdir = os.path.join(os.getcwd(), 'lib')

FITS_LOCATION = "https://hla.stsci.edu/cgi-bin/ecfproxy?file_id=hag_j004524.96+403851.8_j8hpdcaoq_v01.drizzle.fits"

import warnings
from astropy.utils.data import CacheMissingWarning
warnings.simplefilter('ignore', CacheMissingWarning)

from astropy.io import fits

def do_science(fits_location):
    hdul = fits.open(fits_location)
    print(hdul.info())

def handler(event, context):
    do_science(FITS_LOCATION)

if __name__ == "__main__":
    handler('', '')

```

#### What this code should do next

Use something like [`astroquery.mast`](http://astroquery.readthedocs.io/en/latest/mast/mast.html) to query for a collection of files and call the Lambda function for each file (i.e. dynamically pass the location of the FITS file). Then do something clever and write the result to S3?
