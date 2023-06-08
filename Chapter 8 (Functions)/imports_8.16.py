"""
using a program you wrote that has one function in it, store that function in a 
separate file. Import the function into your main program file, and call the
function into your main program file, and call the function using each of these
approaches:

import module_name
from module_name import function_name
from module_name import function_name as fn
import module_name as mn
from module_name import *
"""

from book import favorite_book
from book import favorite_book as fb
from book import *
import book as bk
import book

favorite_book('Python Crash Course')
fb('The Phoenix Project')
bk.favorite_book('Learning How to Learn')
favorite_book('Never Split the Difference')
book.favorite_book('Fierce People')
