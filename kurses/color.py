import math

def hsv_to_rgb(hsv, µ=100):
    h = float(hsv[0]) / µ
    s = float(hsv[1]) / µ
    v = float(hsv[2]) / µ

    i = math.floor(h*6)
    f = h*6 - i
    p = v * (1-s)
    q = v * (1-f*s)
    t = v * (1-(1-f)*s)

    r, g, b = [
        (v, t, p),
        (q, v, p),
        (p, v, t),
        (p, q, v),
        (t, p, v),
        (v, p, q),
    ][int(i%6)]

    return type(µ)(r*µ), type(µ)(g*µ), type(µ)(b*µ)

def hsl_to_rgb(hsl, µ=128):
    h = float(hsl[0]) / µ
    s = float(hsl[1]) / µ
    l = float(hsl[2]) / µ

    def hue_to_rgb(p, q, t):
        t += 1 if t < 0 else 0
        t -= 1 if t > 1 else 0
        if t < 1/6: return p + (q - p) * 6 * t
        if t < 1/2: return q
        if t < 2/3: p + (q - p) * (2/3 - t) * 6
        return p

    if s == 0:
        r, g, b = l, l, l
    else:
        q = l * (1 + s) if l < 0.5 else l + s - l * s
        p = 2 * l - q
        r = hue_to_rgb(p, q, h + 1/3)
        g = hue_to_rgb(p, q, h)
        b = hue_to_rgb(p, q, h - 1/3)

    return type(µ)(r*µ), type(µ)(g*µ), type(µ)(b*µ)

def hex_to_rgb(h, µ=128, µ_=256) :
    assert type(h) in {str, int}, "hex color value must be str or hex int"
    if type(h) == int :
        h = hex(h)[2:]
        while len(h) % 3 != 0 :
            h = "0" + h
    else :
        assert len(h) != 0 and h[0] == "#", "hex color must start with '#'"
        h  = h[1:]
        assert len(h) % 3 == 0, "hex color must contain 3 values with the same size"
        try:
            int(h, 16)
        except:
            raise ValueError("hex color must be an hex int value")
    l   = int(len(h) / 3)
    r, g, b = (int(h[i:i+l], 16) / µ_ for i in (0, l, 2*l))
    return int(r*µ), int(g*µ), int(b*µ)

def rgb_to_hex(rgb, µ=128, µ_=256) :
    r = float(rgb[0]) * µ_/µ
    g = float(rgb[1]) * µ_/µ
    b = float(rgb[2]) * µ_/µ

    r_ = hex(int(r))[2:]
    g_ = hex(int(g))[2:]
    b_ = hex(int(b))[2:]

    l = max(len(r_), len(g_), len(b_))
    while len(r_) != l :
        r_ = "0" + r_
    while len(g_) != l :
        g_ = "0" + g_
    while len(b_) != l :
        b_ = "0" + b_

    return r_ + g_ + b_

def hex_to_hsv(h, µ=128, µ_=256) :
    rgb_to_hsl(hex_to_rgb(h, µ, µ_))

def hex_to_hsl(h, µ=128, µ_=256) :
    rgb_to_hsv(hex_to_rgb(h, µ, µ_))

def hsv_to_hex(h, µ=128, µ_=256) :
    rgb_to_hex(hsv_to_rgb(h, µ), µ_)

def hsl_to_hex(h, µ=128, µ_=256) :
    rgb_to_hex(hsl_to_rgb(h, µ), µ_)

def rgb_to_hsv(rgb, µ=128):
    r = float(rgb[0]) / µ
    g = float(rgb[1]) / µ
    b = float(rgb[2]) / µ

    high = max(r, g, b)
    low = min(r, g, b)
    h, s, v = high, high, high

    d = high - low
    s = 0 if high == 0 else d/high

    if high == low:
        h = 0.0
    else:
        h = {
            r: (g - b) / d + (6 if g < b else 0),
            g: (b - r) / d + 2,
            b: (r - g) / d + 4,
        }[high]
        h /= 6

    return type(µ)(h*µ), type(µ)(s*µ), type(µ)(v*µ)

def rgb_to_hsl(rgb, µ=128):
    r = float(rgb[0]) / µ
    g = float(rgb[1]) / µ
    b = float(rgb[2]) / µ

    high = max(r, g, b)
    low = min(r, g, b)
    h, s, v = ((high + low) / 2,)*3

    if high == low:
        h = 0.0
        s = 0.0
    else:
        d = high - low
        s = d / (2 - high - low) if l > 0.5 else d / (high + low)
        h = {
            r: (g - b) / d + (6 if g < b else 0),
            g: (b - r) / d + 2,
            b: (r - g) / d + 4,
        }[high]
        h /= 6

    return type(µ)(h*µ), type(µ)(s*µ), type(µ)(v*µ)

def hsv_to_hsl(hsv, µ=128):
    h = float(hsv[0]) / µ
    s = float(hsv[1]) / µ
    v = float(hsv[2]) / µ

    l = 0.5 * v  * (2 - s)
    s = v * s / (1 - math.fabs(2*l-1))
    return type(µ)(h*µ), type(µ)(s*µ), type(µ)(l*µ)

def hsl_to_hsv(hsl, µ=128):
    h = float(hsl[0]) / µ
    s = float(hsl[1]) / µ
    l = float(hsl[2]) / µ

    v = (2*l + s*(1-math.fabs(2*l-1)))/2
    s = 2*(v-l)/v
    return type(µ)(h*µ), type(µ)(s*µ), type(µ)(v*µ)