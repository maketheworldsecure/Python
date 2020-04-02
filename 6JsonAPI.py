#! usr/bin/env python

import json
Rawdata = {'Hello': 5, 'Wow': 7, 'Covid': 3, 'Made': 4, 'in': 3, 'china': 4}
print("Raw data :")
print(Rawdata)
print("\nJSON format:")
print(json.dumps(Rawdata,indent=1))
