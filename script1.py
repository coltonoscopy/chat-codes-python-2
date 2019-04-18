'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, 
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''

import time, sys, os                        # puppet4411

def project():                              # sohazur
    # AMENDMENT: m_brax
    x = 0                                   # 1tracksystem
    for i in range(1000):                   # Kolompouras
        if (i % 3 == 0) or (i % 5 == 0):    # kaunaj
            x += i                          # thechocokid21
            print(i)                        # unknownboyak
    print(x)                                # abhi_tch_18

project()                                   # dancetrainer