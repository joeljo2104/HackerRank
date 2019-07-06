def count_substring(string, sub_string):
    c=0
    for i in range(0,len(string)-len(sub_string)+1):
        a=''
        if string[i]==sub_string[0]:
            a=string[i:i+len(sub_string)]
            if a==sub_string:
                c+=1
    return c

