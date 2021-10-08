import rx

def push_five_strings(observer):
    observer.on_next("Alpha")
    observer.on_next("Beta")
    observer.on_next("Gamma")
    raise Exception('err')
    observer.on_next("Delta")
    observer.on_next("Epsilon")
    observer.on_completed()

def skiperr(x):
    try:
        x()
    except:
        return x

# class PrintObserver():
# class PrintObserver(Observer):

#     def on_next(self, value):
#         print("Received {0}".format(value))

#     def on_completed(self):
#         print("Done!")

#     def on_error(self, error):
#         print("Error Occurred: {0}".format(error))


source = rx.create(push_five_strings)
source.pipe(skiperr).subscribe(    
    on_next = lambda x: print("Received {x}"),
    on_completed = print("Done!"),
    on_error= lambda error: print("Error Occurred: {0}".format(error))
)
