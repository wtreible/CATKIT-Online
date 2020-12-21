########################################
# Utility Functions for the CATKit API #
########################################

def good_request(data):
  return {'status' : 'OK', 'code' : 200, 'data' : data}
  
def bad_request(message):
  return {'status' : 'BAD REQUEST', 'code' : 400, 'message' : message}

def parse_search(search_data, term_fn, pair_sep='=', term_sep='+', not_char='!'):

  if pair_sep not in search_data:
    return bad_request("Request must contain '{}' to indicate a key{}value pair".format(pair_sep, pair_sep))

  data = search_data.split('+')
  if not all([d.count(pair_sep)==1 for d in data]):
    return bad_request("All request pairs must contain only one '{}' per key{}value pair".format(pair_sep, pair_sep))
  else:
    out_data = {}
    search_terms = []
    for d in data:
      tmp = d.split('=')
      if tmp[0][-1] == not_char:
        key = tmp[0][:-1]
        value = not_char + tmp[1]
      else:
        key = tmp[0]
        value = tmp[1]
      
      if not key.isalpha():
        return bad_request("Key: {} is not a valid character string".format(key))
      if key in out_data.keys():
        return bad_request("Key: {} occurs multiple times in the input".format(key))
      if (value[0] == not_char and not value[1:].isalpha()):
        return bad_request("Value: {} is not a valid character string when using {}=".format(value[1:], not_char))
      if (value[0] != not_char and not value.isalpha()):
        return bad_request("Value: {} is not a valid character string".format(value))
        
      out_data[key] = value
      search_terms += [key, value]
    
  
    search_ids = term_fn(search_terms)
    return good_request({'ids': search_ids, 'request':out_data})