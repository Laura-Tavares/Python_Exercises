def calculate_love_score(name1, name2):
    
    combined = name1 + name2
    lower_names = combined.lower()
    
    t = lower_names.count("t")
    r = lower_names.count("r")
    u = lower_names.count("u")
    e = lower_names.count("e")
    n1 = t + r + u + e
    
    l = lower_names.count("l")
    o = lower_names.count("o")
    v = lower_names.count("v")
    e = lower_names.count("e")
    n2 = l + o + v + e
    
    score = str(n1) + str(n2)
    print(score)

calculate_love_score("Name1", "Name2")
