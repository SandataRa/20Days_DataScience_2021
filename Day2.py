#Task N°6
g_x = 2.5
 
def f1(x):
    global g_x
    y = 6
    g_x = x * y
    return g_x
 
# Attempt to reference a function's local variable outside of the function
# print(y)
 
print(f1(5))
print(g_x)
 
print(f1(g_x))
print(g_x)
 
#Task N°7
def my_function( *args , **kwargs):
    first_element = args[0]
    list_shops = {}
    for e in kwargs.items():
        list_shops[e[0]] = e[1]
 
    return { "first_element": first_element,
             "named_arguments": list_shops }
 
results = my_function(["Apple","Banana","Strawberry"], shop1="Auchan", shop2="Carrefour", shop3="Lidll", shop4="LeClerc")            
print(results)
 
#Task N°8 
def greet_hello(name):
    def hello():
        print("Hello ", name)
    return hello
 
h = greet_hello("Sophie")
h()
h = greet_hello("Kyle")
h()
