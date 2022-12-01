def write_history(s, a, b, res):
    file = open('history_file.txt', 'a', encoding = "UTF - 8")
    file.write(str(a) +' '+ str(s) +' '+str(b)+' = '+str(res)+'\n')
    file.close()