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
