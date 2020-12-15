from datetime import date 

def isSlotAvailable(approved_leaves, request_leaves):
    tim = []
    leaf = request_leaves['leaveFrom']
    leaf = list(map(int, leaf.split('-')))
    leaf = date(leaf[2],leaf[1] ,leaf[0]) 
    leat = request_leaves['leaveUpto']
    leat = list(map(int, leat.split('-')))
    leat = date(leat[2],leat[1] ,leat[0])
    
    for i in range(approved_leaves):
        f = i['leaveFrom']
        f = list(map(int, f.split('-')))
        t = i['leaveUpto']
        t = list(map(int, t.split('-')))
        x = date(f[2],f[1] ,f[0]) 
        y = date(t[2],t[1] ,t[0])
        if x<=leaf<=y of x<=leat<=y:
            return False
    return True
        
