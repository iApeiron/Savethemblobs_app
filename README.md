# Savethemblobs_app


Easily save/manage SHSH blobs from Apple and Cydia

iOS Port of [Savethemblobs](https://www.github.com/iApeiron/savethemblobs)

Based on omz’s opensource [Python Framework](https://github.com/omz/PythonistaAppTemplate)

Thanks to [ccclauss](https://github.com/cclauss) for help with main.py

This is currently a working beta.


## Usage

    required arguments:
        ecid                 device ECID in int or hex (prefix hex with 0x)
        device               device identifier/boardconfig (eg. iPhone3,1 or n90ap)

    optional arguments:
        -h, --help           show this help message and exit
        --save-dir SAVE_DIR  local dir for saving blobs (default: ~/Documents/.shsh)
        --overwrite          overwrite any existing blobs
        --overwrite-apple    overwrite any existing blobs (only from Apple)
        --overwrite-cydia    overwrite any existing blobs (only from Cydia)
        --no-submit-cydia    don't submit blobs to Cydia server
        --cydia-blobs        fetch blobs from Cydia server (32 bit devices only)


Here is a compiled [sideloadable IPA](http://www.mediafire.com/file/laio3ud311xxghc/Savethemblobs.ipa)

Blobs are saved by default to shsh inside the app’s own Documents folder, easily accessed through iTunes or iFunbox.


Anybody interested in improving this is welcome to contribute.
