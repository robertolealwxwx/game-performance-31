def calculate_fps(frames, time):
    """Calculate frames per second (FPS)"""
    if time <= 0:
        return 0
    return frames / time


def clamp(value, min_value, max_value):
    """Clamp a value to a given range"""
    return max(min(value, max_value), min_value)


def load_image(file_path):
    """Load an image from the given file path"""
    from PIL import Image
    try:
        return Image.open(file_path)
    except FileNotFoundError:
        raise Exception(f'Image not found: {file_path}')


def check_collision(rect_a, rect_b):
    """Check if two rectangles collide"""
    return (rect_a['x'] < rect_b['x'] + rect_b['width'] and
            rect_a['x'] + rect_a['width'] > rect_b['x'] and
            rect_a['y'] < rect_b['y'] + rect_b['height'] and
            rect_a['y'] + rect_a['height'] > rect_b['y'])


def smooth_step(edge0, edge1, x):
    """Smooth step interpolation"""
    if x < edge0:
        return 0
    if x > edge1:
        return 1
    t = (x - edge0) / (edge1 - edge0)
    return t * t * (3 - 2 * t)