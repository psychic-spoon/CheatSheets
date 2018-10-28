import json
import gzip 


#Making gzip
################################################################
json_str = json.dumps(data) + "\n"               # 2. string (i.e. JSON)
json_bytes = json_str.encode('utf-8')            # 3. bytes (i.e. UTF-8)

with gzip.GzipFile(jsonfilename, 'w') as fout:   # 4. gzip
    fout.write(json_bytes)                       
# Note that adding "\n" is completely superfluous here. It does not break anything, but beyond that it has no use.

#Reading gzip
#################################################################
# Reading works exactly the other way around:
with gzip.GzipFile(jsonfilename, 'r') as fin:    # 4. gzip
    json_bytes = fin.read()                      # 3. bytes (i.e. UTF-8)

json_str = json_bytes.decode('utf-8')            # 2. string (i.e. JSON)
data = json.loads(json_str)                      # 1. data

print(data)
# Of course the steps can be combined:

#Short Steps
#########################################################
with gzip.GzipFile(jsonfilename, 'w') as fout:
    fout.write(json.dumps(data).encode('utf-8'))                       
# and

with gzip.GzipFile(jsonfilename, 'r') as fin:
    data = json.loads(fin.read().decode('utf-8'))