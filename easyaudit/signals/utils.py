import inspect

def caller_name(skip=2):
    """Get the name of the calling function in the format module.class.method.

    The `skip` parameter specifies how many levels of stack to skip while getting
    the caller name. `skip=1` means "who calls me", `skip=2` means "who calls my
    caller" etc.

    An empty string is returned if the skipped levels exceed the stack height.
    """
    stack = inspect.stack()
    start = 0 + skip
    if len(stack) < start + 1:
        return ""

    for i in range(start, len(stack)):
        frame = stack[i][0]
        code = frame.f_code
        if code.co_name != "<listcomp>":
            module = inspect.getmodule(code)
            class_name = ""
            if "self" in frame.f_locals:
                class_name = frame.f_locals["self"].__class__.__name__
            return f"{module.__name__}.{class_name}.{code.co_name}"

    return ""