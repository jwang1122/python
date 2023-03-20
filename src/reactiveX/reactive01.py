from rx import of, operators as op

# Create an observable that emits the numbers 1 to 5
source = of(1, 2, 3, 4, 5)

# Modify the observable to square each emitted value
squared = source.pipe(
    op.map(lambda value: value ** 2)
)

# Subscribe to the observable and print out each emitted value
squared.subscribe(
    on_next=lambda value: print(f"Received value: {value}"),
    on_error=lambda error: print(f"Received error: {error}"),
    on_completed=lambda: print("Observable completed")
)
