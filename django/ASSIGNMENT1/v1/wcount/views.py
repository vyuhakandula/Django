from django.shortcuts import render
from django.shortcuts import HttpResponse
import operator
def home(requests):
    return HttpResponse('<h1> This is the first page</h1>')
def about(requests):
    return HttpResponse('<h1> about </h1><ul><li>B.Pranith</li><li> 1602-18-737-029</li></ul>')
def hobbies(requests):
    return HttpResponse('<h1> Hobbies</h1><ol><li>Watching webseries</li></ol>')
