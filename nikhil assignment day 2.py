Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #list and its default functions
>>> ls = ["nikhil",1,2,3,4,5,"kethe"]
>>> print(ls)
['nikhil', 1, 2, 3, 4, 5, 'kethe']
>>> ls.append("kethe")
>>> print(ls)
['nikhil', 1, 2, 3, 4, 5, 'kethe', 'kethe']
>>> ls.copy()
['nikhil', 1, 2, 3, 4, 5, 'kethe', 'kethe']
>>> ls.count("kethe")
2
>>> ls.index(1)
1
>>> ls.insert(2,43)
>>> print(ls)
['nikhil', 1, 43, 2, 3, 4, 5, 'kethe', 'kethe']
>>> ls.pop(2)
43
>>> print(ls)
['nikhil', 1, 2, 3, 4, 5, 'kethe', 'kethe']
>>> ls.reverse()
>>> print(ls)
['kethe', 'kethe', 5, 4, 3, 2, 1, 'nikhil']
>>> #dictiionary and its functions
>>> dct = {"name":"nikhil","age":"18","schl":"naryana english medium high school","phno":"234123321"}
>>> print(dct)
{'name': 'nikhil', 'age': '18', 'schl': 'naryana english medium high school', 'phno': '234123321'}
>>> dct.fromkeys()
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    dct.fromkeys()
TypeError: fromkeys expected at least 1 argument, got 0
>>> dct.get("name")
'nikhil'
>>> dct.items()
dict_items([('name', 'nikhil'), ('age', '18'), ('schl', 'naryana english medium high school'), ('phno', '234123321')])
>>> dct.keys()
dict_keys(['name', 'age', 'schl', 'phno'])
>>> dct.pop("name")
'nikhil'
>>> print(dct)
{'age': '18', 'schl': 'naryana english medium high school', 'phno': '234123321'}
>>> dct.values()
dict_values(['18', 'naryana english medium high school', '234123321'])
>>> #sets and its default functions
>>> st = {1,1,1,2,3,3,4,4,5,5,6,6,7,8,9,10}
>>> print(st)
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
>>> st.add(123)
>>> print(st)
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 123}
>>> st1 ={21,23,43,54,56,55,5,4,3,4,5}
>>> st.difference(st1)
{1, 2, 6, 7, 8, 9, 10, 123}
>>> st.difference_update()
>>> print(st)
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 123}
>>> #sir i am unable to find out how sets peforms its default functions so please i am requesting to tell about sets functions clearly in live..
>>> stri = ("nikhil")
>>> print(stri)
nikhil
>>> stri.capitalize()
'Nikhil'
>>> stri.count("nikhil")
1
>>> stri.title()
'Nikhil'
>>> stri.split()
['nikhil']
>>> stri.find("nikhil")
0
>>> stri.join(1)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    stri.join(1)
TypeError: can only join an iterable
>>> # sir extremely tough using string default methods could you please suggest a way for this to find out the use of each and every method
>>> 