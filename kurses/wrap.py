import textwrap

def wrap(s, w, oneline=False) :
    wrapped = textwrap.wrap(s, w)
    if len(wrapped) == 0 :
        wrapped.append("")
    if oneline and len(wrapped) == 1 :
        return wrapped, len(wrapped[0])
    wrapped = [i + " " * (w - len(i)) for i in wrapped]
    return wrapped, len(wrapped[0])