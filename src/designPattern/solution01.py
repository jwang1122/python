
from rx import Observable, Observer
from rx.internal import extensionmethod

class ExRx:
    
    def __init__(self, value = None, error = None):
        self._value = value
        self._error = error
        return super().__init__()        

    @property
    def Value(self):
        return self._value

    @property
    def Error(self):
        return self._error

    @classmethod
    def RxValue(cls, value):
        return cls(value)

    @classmethod
    def RxError(cls, error):
        return cls(None, error)

@extensionmethod(Observable)
def subscribe_ex(source, on_next_value, on_error):

    def on_next(s):
        if s != None:
            if s.Error != None:
                on_error(s.Error)
            else:
                try:
                    on_next_value(s.Value)
                except:
                    on_error(s.Error)
     
    def on_completed():
        pass

    return source.subscribe(on_next, on_error, on_completed)

@extensionmethod(Observable)
def continue_on_error(source):
    def subscribe(observer):

        def on_next(item):
            observer.on_next(ExRx.RxValue(item))
            
        def on_error(error):
            observer.on_next(ExRx.RxError(error))
            observer.on_completed()

        def on_completed():
            observer.on_completed()

        return source.subscribe(on_next=lambda x: on_next(x), on_error=lambda y: on_error(y), on_completed=lambda: on_completed())

    return Observable.create(subscribe)

@extensionmethod(Observable)
def map_ex(source, selector):
    def mapex(item):
        try:
            return ExRx.RxValue(selector(item.Value))
        except Exception as error:
            return ExRx.RxError(error)

    return source.map(mapex)

def printsequence():
    seq = Observable.from_(range(10)) \
            .continue_on_error() \
            .map_ex(throw_exception_when5) \
            .subscribe_ex(print, print)

def throw_exception_when5(x):
    if x == 5:
        raise ValueError('Boooooo... Something went wrong here !')
    return x

if __name__ == '__main__':
    printsequence()

