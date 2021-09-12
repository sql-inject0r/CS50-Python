def announce(f):
i    def wrapper():
        print("Gonna run the function")
        f()
        print("Done with the function")
    return wrapper

@announce 
def hello():
 i   print("Hello world !")

hello()
