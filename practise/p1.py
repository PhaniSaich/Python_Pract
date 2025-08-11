a = 5

def fn_even_odd(ele):
  if ele%2 == 0:
    print(ele, " - is even")
  else:
    print(ele, " - is odd")
  
fn_even_odd(a)
fn_even_odd(ele=a)

a = [1,2,3,4]
for ele in a:
  fn_even_odd(ele=ele)

