def calculate_fps(frames, time_elapsed):
    """
    Calculate frames per second given the number of frames
    and the elapsed time.
    """
    if time_elapsed <= 0:
        return 0
    return frames / time_elapsed


def clamp(value, min_value, max_value):
    """
    Restrict a value to be within min and max limits.
    """
    return max(min(value, max_value), min_value)


def load_image(file_path):
    """
    Load an image from a specified file path.
    """
    from PIL import Image
    try:
        img = Image.open(file_path)
        return img
    except IOError:
        print(f'Error loading image: {file_path}')
        return None


def interpolate_color(color1, color2, factor):
    """
    Interpolate between two RGB colors based on a factor.
    """
    return (
        int(color1[0] + (color2[0] - color1[0]) * factor),
        int(color1[1] + (color2[1] - color1[1]) * factor),
        int(color1[2] + (color2[2] - color1[2]) * factor)
    )


def save_to_file(data, file_path):
    """
    Save data to a file in JSON format.
    """
    import json
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)

