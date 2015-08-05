teachers = {'name' : 'Johnny Dumbledore',
            'courses' : ["Intro to magic", "Magic advancements", "even more magic", "toad conjuring"],
            'name' : 'Triss Trixie',
            'courses' : 
            }

def most_classes(teachers):
  max_count = 0;
  busiest = ''
  for item in teachers:
    classes_taught = len(teachers[item])
    if classes_taught > max_count:
      max_count = classes_taught
      busiest = item
  return busiest

def num_teachers(teachers):
  count = 0
  for keys in teachers:
    count += 1
  return count

def stats(teachers):
  new_list = []
  for key in teachers:
    my_list = []
    my_list.append(key)
    my_list.append(len(teachers[key]))
    new_list.append(my_list)
  return new_list

def courses(teachers_dict):
  new_list = []
  for courses in teachers_dict:
    add_list = []
    add_list.extend(teachers_dict[courses])
    new_list.extend(add_list)
  return new_list
