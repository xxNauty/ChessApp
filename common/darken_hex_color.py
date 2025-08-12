def darken_hex_color(hex_color: str, factor: float = 0.7):
    hex_color = hex_color.lstrip('#')
    rgb = [int(hex_color[i:i+2], 16) for i in (0, 2, 4)]
    darker_rgb = [int(c*factor) for c in rgb]
    return '#' + ''.join(f'{c:02x}' for c in darker_rgb)