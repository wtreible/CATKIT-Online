import os, sys
basedir = "/data/CAT/"
catlib_dir = os.path.join(basedir, "CATKIT/CATKit/sdk/catlib/")
sys.path.append(catlib_dir)

# Cat API Utils and CAT lib imports
from cat_db import CatDB
from cat_api_utils import *

catdb = CatDB()

# Flask Imports
from flask import Flask, jsonify, send_file
app = Flask(__name__)
                
#################
# API Endpoints #
#################
@app.route('/')
def api_root():
  return 'API Root'

@app.route('/search/<search_data>')
def search(search_data):

  parsed_search = parse_search(search_data)
  
  search_terms = []
  for k,v in parsed_search['data'].iteritems():
    search_terms += [k,v]

  label_img_ids = catdb.multisearch(search_terms)
  return str(label_img_ids)

@app.route('/get_image/<image_id>')
def get_image(image_id):
  try:
    dbitem = catdb[int(image_id)]
    return send_file(dbitem['path'], mimetype='image/png')
  except:
    return jsonify(bad_request("Image ID not valid."))