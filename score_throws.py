# scoreThrows( [1, 5, 11] )    =>  15

def score_throws(radii):
    pts = 0
    times = 0
    if not radii:
        return 0
    
    for i in radii:
        if i < 5:
            pts += 10
        elif i >= 5 and i <= 10:
            pts += 5
            
    for i in radii:
        if i < 5:
            times += 1
            
    if len(radii) == times:
        pts += 100
        
    return pts
        
            
