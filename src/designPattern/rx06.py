import rx
from rx import operators as ops

rx.of("Alpha", "Beta", "Gamma", "Delta", None, "Epsilon").pipe(
ops.map(lambda s: len(s)),
ops.filter(lambda i: i >= 5)
).subscribe(
    on_next = lambda value: print("Received {0}".format(value)),
    on_error = lambda e: print("Error : {0}".format(e)),
    on_completed = lambda: print("Done!"),
)

