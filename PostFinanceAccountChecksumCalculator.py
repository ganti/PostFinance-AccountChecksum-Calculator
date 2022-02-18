#!/usr/bin/env python3
 
def PostFinanceAccountChecksumCalculator(prefix: str, base: str):
    """
    prefix: two digit number, e.g. 30,60,80,90
    base: number between 0 and 999'999 (e.g, 177451)
    return: checksum (e.g 1) => prefix + base + checksum => 61-177451-1
    """
    prefix = str(prefix)
    base = str(base)

    if len(prefix) != 2 or len(base) > 6:
        return False
    if len(base) < 6:
        base = base.zfill(6)
    numb = prefix + base

    transfer = 0
    perm = [0, 9, 4, 6, 8, 2, 7, 1, 3, 5]
    for c in numb:
        index = ( int(c) + transfer ) % 10
        transfer = perm[index]
    checksum = int((10-transfer) % 10)
    return checksum
