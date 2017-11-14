# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def index(request):
    data=[]
    method = ""
    if request.method == 'GET':
        data = request.GET
        method = 'Get'
    if request.method == 'POST':
        data = request.POST
        method = 'Post'
    return render(request, 'index.html', {
        'method' : method,
        'data' : data
    })