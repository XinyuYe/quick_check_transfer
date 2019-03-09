# Check JI transfer course by pdf
## usage:
### Step 1
open the transcript and export it as plain pdf (to decrypt it). 
In mac: file/export as pdf...

### Step 2
```
git clone https://github.com/XinyuYe/quick_check_transfer.git
python3 -m venv ./env
source env/bin/activate
pip install -r requirements.txt
python pdf.py SSR_TSRPT_SC.pdf

```
### Others
Currently only support one page of unofficial transcript
