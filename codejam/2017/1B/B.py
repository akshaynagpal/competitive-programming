num_tests = int(raw_input())

for test in range(num_tests):
  colordict = {}
  temp = map(int,raw_input().split())
  n = temp[0]
  colordict['R'] = temp[1]
  colordict['ORY'] = temp[2]
  colordict['Y'] = temp[3]
  colordict['GYB'] = temp[4]
  colordict['B'] = temp[5]
  colordict['VRB'] = temp[6]
  total_colors = 0
  if colordict['R']>0:
    total_colors += 1
  if colordict['Y']>0:
    total_colors += 1
  if colordict['B']>0:
    total_colors += 1
  max_num = n/total_colors
  temp_keys = colordict.keys()
  possible = True
  for k in temp_keys:
    if colordict[k]>max_num:
      possible = False
    elif colordict[k]>1 and colordict[k]==max_num and total_colors==1:
      possible = False
  
  if possible:
    ranks = []
    i = 0
    for k in temp_keys:
      if colordict[k]>0 and k not in ranks:
        ranks.append(k)
    count = 0
    perm = []
    temp_len = len(ranks)
    while count<n:
      for i in range(temp_len):
        if colordict[ranks[i]]>0:
          perm.append(ranks[i])
          colordict[ranks[i]] -= 1
          count += 1
    print 'Case #'+str(test+1)+': '+''.join(perm)
  else:
    print 'Case #'+str(test+1)+': '+'IMPOSSIBLE'