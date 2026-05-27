import time

def optimized_heavy_computation(data):
    result = []
    start_time = time.time()
    for item in data:
        # Replace an expensive operation with a more efficient one
        processed_item = process_item(item)
        result.append(processed_item)
    end_time = time.time()
    print(f"Processing took {end_time - start_time:.4f} seconds")
    return result


def process_item(item):
    # Efficient computation logic
    # Assuming item is a dictionary with numerical values
    return {key: value * 2 for key, value in item.items()}


if __name__ == "__main__":
    sample_data = [{"a": 1, "b": 2}, {"a": 3, "b": 4}]
    optimized_heavy_computation(sample_data)