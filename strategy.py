import random 
def create(l: list):
  u = lambda l: sorted(l)
  l = u(l)

  def append(i):
    l.append(i)
  def set_sort(sorter):
    nonlocal u
    u = sorter
  def sort():
    nonlocal l
    l = u(l)
  def get():
    nonlocal l
    return l 

  return append, set_sort, sort,get

append, set_sort, sort, get = create (["A","B", "C","D"])

sort()
print(get())

set_sort(lambda x: sorted(x, reverse=True))
sort()
print(get())

set_sort(lambda x:sorted (x, key = lambda _:  random.random()))
sort()
print(get())