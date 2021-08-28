import rx

# create lowercase operator
def lowercase():
    def _lowercase(source): # common way to implement custom operator
        def subscribe(observer, scheduler = None):
            def on_next(value):
                if len(value) < 5:
                    raise Exception("Length less than 5.")
                observer.on_next(value.lower())
            return source.subscribe(
                on_next,
                observer.on_error,
                observer.on_completed,
                scheduler)
        return rx.create(subscribe)
    return _lowercase

rx.of("Alpha", "Beta", "Gamma", "Delta", "Epsilon").pipe(
lowercase()
).subscribe(
    on_next = lambda value: print("Received {0}".format(value)),
    on_error = lambda e: print(f"Error: {e}")
)

