import time as t

dic={} 

def create_key(k,val,time_val=0):
    if k in dic:
        print("Error:\"",k,"\" - key already exists")
    else:
        if(k.isalpha()):
            if len(dic)<(1024*1024*1024) and val<=(16*1024*1024): 
                if time_val==0:
                    l=[val,time_val]
                else:
                    l=[val,t.time()+time_val]
                if len(k)<=32: 
                    dic[k]=l
                print("\"",k,"\" Key-value created successfully")
            else:
                print("Error: Memory limit exceeded ")
        else:
            print("Error :\"",k,"\" - Invalid key name")

            
def read_value(k):
    if k not in dic:
        print("Error :\"",k,"\" - key does not exist")
    else:
        z=dic[k]
        if z[1]!=0:
            if t.time()<z[1]: 
                out=str(k)+":"+str(z[0])
                #print(out)
                return out
            else:
                print("Error : Time-to-live of the \"",k,"\" has expired")
        else:
            out=str(k)+":"+str(z[0])
            #print(out)
            return out

def delete_key(k):
    if k not in dic:
        print("Error :\"",k,"\" - key does not exist")
    else:
        z=dic[k]
        if z[1]!=0:
            if t.time()<z[1]: 
                del dic[k]
                print("\"",k,"\" - Key is successfully deleted")
            else:
                print("Error : Time-to-live of the \"",k,"\" has expired")
        else:
            del dic[k]
            print("\"",k,"\"- Key is successfully deleted")

def modify_value(k,val):
    z=dic[k]
    if z[1]!=0:
        if t.time()<z[1]:
            if k not in dic:
                print("Error :\"",k,"\" -key does not exist")
            else:
                l=[]
                l.append(val)
                l.append(z[1])
                dic[k]=l
        else:
            print("Error : Time-to-live of the \"",k,"\" has expired")
    else:
        if k not in dic:
            print("Error :\"",k,"\" -key does not exist")
        else:
            l=[]
            l.append(val)
            l.append(z[1])
            dic[k]=l

