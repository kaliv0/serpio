from functools import wraps

from fumus.utils import Optional, Result


def returns_optional(func):
    @wraps(func)
    def wrapper(*args, **kw):
        return Optional.of_nullable(func(*args, *kw))

    return wrapper


def returns_result(func):
    @wraps(func)
    def wrapper(*args, **kw):
        # TODO: receive custom list of exceptions form user
        #  do we need BaseException
        #  what if we have more complex scenario with multiple errors etc?
        try:
            result = func(*args, *kw)
        except (Exception, BaseException) as err:
            return Result.failure(err)
        return Result.success(result)

    return wrapper
