

def mixly_mapping(v, al, ah, bl, bh):
    return bl + (bh - bl) * (v - al) / (ah - al)


print(mixly_mapping(60, 50, 80, 56, 74))