from pymonad.either import Left, Right, Either
from pymonad.tools import curry


@curry(2)
def divide(a, b) -> Either[str, float]:
    if b == 0:
        return Left("Division by zero error")
    else:
        return Right(a / b)


def handle_result(result: Either[str, float]):
    result.either(
        lambda error: print(f"Error: {error}"),
        lambda value: print(f"The result is: {value}"),
    )


result1 = divide(10)(2)  # result1: Either[str, float] = Right(5.0)
result2 = divide(10)(0)  # result2: Either[str, float] = Left('Division by zero error')

handle_result(result1)  # prints "The result is: 5.0"
handle_result(result2)  # prints "Error: Division by zero error"
