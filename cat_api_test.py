import os, sys
basedir = "/data/CAT/"
catlib_dir = os.path.join(basedir, "CATKIT/CATKit/sdk/catlib/")
sys.path.append(catlib_dir)

# Cat API Utils and CAT lib imports
from cat_db import CatDB
from cat_api_utils import parse_search

catdb = CatDB()

def search(search_data):

  parsed_search = parse_search(search_data, term_fn=catdb.multisearch)
  
  search_terms = []
  for k,v in parsed_search['data'].iteritems():
    search_terms += [k,v]


  label_img_ids = catdb.multisearch(search_terms)
  return str(len(label_img_ids))


