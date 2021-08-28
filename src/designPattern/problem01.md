# Skip the error and continue

```py
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
    return Observable.just(x).catch_exception(lambda e: Observable.just(1))

class PrintObserver(Observer):

    def on_next(self, value):
        print("Received {0}".format(value))

    def on_completed(self):
        print("Done!")

    def on_error(self, error):
        print("Error Occurred: {0}".format(error))

source = rx.create(push_five_strings)
source.flat_map(skiperr).subscribe(PrintObserver())
```