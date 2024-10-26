x = 20
def function():
    global x
    x = 10
    print("x function:", x)

print("x outside 1:", x)
function()
print("x outside:", x)
