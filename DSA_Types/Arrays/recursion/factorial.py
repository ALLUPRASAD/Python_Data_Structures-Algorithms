def reec(m):
    assert m>=0 and int(m)==m
    if m in [0,1]:
        return m
    else:
        return m*reec(m-1)
