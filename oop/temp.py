
works = """pen                    pencil                         pencil-case   
ruler ['ru:lə]               eraser [i'reizə]                          crayon ['kreiən]
book [buk]                     bag [[bæɡ]                               sharpener ['ʃɑ:pənə]
school [sku:l]              head [hed]                                   face[feis]
nose[nəuz]                 mouth [mauθ]                              eye[ai]
"""


w1 = works.split('\n')

for s in w1:
    t1 = s.split('   ')
    t2 = []
    for t in t1:
        if t == '':
            continue
        t2.append(t.strip())
        
    temp_list = [' '] * 100
    for idx in range(0, len(t2)):
        from_idx = idx * 30
        for c in t2[idx].strip():
            temp_list[from_idx] = c
            from_idx += 1
    
    print(''.join(temp_list))