for ad in range (0,1001):
    for int in range (2,ad):
        if ad % int == 0:
            break
    else:
        print(ad)
