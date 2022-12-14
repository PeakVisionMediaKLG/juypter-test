#!/usr/bin/env python
# -*- coding: utf-8 -*-

K = float(input("Starting capital? "))
interest_rate = float(input("Interest rate? "))
inflation_rate = float(input("Inflation rate? "))
tax_rate = int(input("taxation in percent "))
n = int(input("Number of years? "))

K_today = K
i = 0
while (i < n):
    interest = K * interest_rate/ 100.0
    interest_after_tax = interest - interest * tax_rate / 100.0
    K += interest_after_tax
    K_today = (K_today + interest_after_tax) * 100 / (100 + inflation_rate)
    i += 1
    print(i,K, K_today)
print("Capital after " + str(n) + " years: " + str(K))
