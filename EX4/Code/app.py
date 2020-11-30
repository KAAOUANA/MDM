# flask_web/app.py

From flask import Flask
app = Flask(__name__)


import sys
from SparseArray import SparseArray
import os


@app.route('/')
def main(config_arg): 
  print("Start exercice 'Maisons du monde'")
  strings=['ab','adc','ab','adc','adc','aa','bb','ab']
  x = SparseArray(strings)
  if False :
	  import os 
	  print("using config for {}".format(config_arg))
	  print (config_arg)
	  queries = config_arg
	  print (queries[0])
	  queries = queries[0].split(",")
	  print (queries)
	  #do decompose element to multi-variable by ','
  queries=['abk','adc','ab']
  print(x.matchingStrings(queries))
  return x.matchingStrings(queries)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
	

