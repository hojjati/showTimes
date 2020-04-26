# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect


def listView(request):
    return redirect('http://localhost:8000/static/list.html')
