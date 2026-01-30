def mask_creditcard(card_number):
    masked="*" *(len(card_number)-4)+card_number[-4:]
    return masked
card="11122224445555030"
print(mask_creditcard(card))
