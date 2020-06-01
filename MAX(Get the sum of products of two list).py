#!/usr/bin/env python
# coding: utf-8
# maximum value for ads  == sort and multiply ! That'll get the maximum value ! 


n = int(input())


a =[int(i) for i in input().split()]



b =[int(i) for i in input().split()]

a.sort()
b.sort()

ans = sum(a[i]*b[i] for i in range(n))


ans



