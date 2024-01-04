

def input_list(lis):
    lis.sort(key=lambda a:len(a) )
    return lis
  
  
  input:lis=['a','aa','a','aaaa','aaaaaa','dfdf']
  output:['a', 'a', 'aa', 'aaaa', 'dfdf', 'aaaaaa']
  
    
