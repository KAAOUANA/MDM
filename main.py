import sys
from SparseArray import SparseArray
import os



def main(config_arg): 
  print("Start exercice 'Maisons du monde'")
  strings=['ab','abc','ab','adc','adc','aa','bb','ab']
  x = SparseArray(strings)
  if True :
	  import os 
	  print("using config for {}".format(config_arg))
	  print (config_arg)
	  queries = config_arg
	  print (queries[0])
	  queries = queries[0].split(",")
	  print (queries)
	  print(x.matchingStrings(queries))
	  #do decompose element to multi-variable by ','
  queries=['abk','adc','ab']
  print(x.matchingStrings(queries))


if __name__ == "__main__":
    main(sys.argv[1:])
	

