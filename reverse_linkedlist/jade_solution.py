def get_data_list(data):
  data_list = []
  data_list.append(data['data'])
  next_node = data['next']
  while inner_dict is not None:    
      node_data = next_node['data']
      data_list.append(node_data)
      next_node = next_node['next']
  return data_list

def make_dict(current_data, prev_dict):
    return {
        'data':current_data,
        'next': prev_dict
}

def reverse_linked_list(data):
  data_list = get_data_list(data)
  for i,e in enumerate(data_list):
      if not i:
          prev_dict = None
          new_dict = make_dict(e, prev_dict)
      else:
          new_dict = make_dict(e, new_dict)
  return new_dict

one = {
    'data': 1,
    'next': {
        'data': 2,
        'next': {
            'data': 3,
            'next': None
            
        }
    }
}

reversed_linked_list = reverse_linked_list(one)
print(reversed_linked_list)