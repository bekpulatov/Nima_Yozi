# from PIL import Image
# import numpy as np
# from collections import defaultdict
#
#
# def get_dominant_colors(image_path, num_colors=2):
#     # Open the image
#     img = Image.open(image_path)
#
#     # Convert image to RGB if it's not
#     img = img.convert('RGB')
#
#     # Get image data
#     img_data = np.array(img)
#
#     # Reshape the image data to a 2D array of pixels
#     pixels = img_data.reshape(-1, 3)
#
#     # Use numpy's unique function with return_counts to get color frequencies
#     unique_colors, counts = np.unique(pixels, axis=0, return_counts=True)
#
#     # Sort colors by frequency
#     sorted_colors = sorted(zip(unique_colors, counts), key=lambda x: x[1], reverse=True)
#
#     # Return the top num_colors
#     return [color for color, count in sorted_colors[:num_colors]]
#
#
# def classify_messages(image_path):
#     # Get the two most dominant colors
#     dominant_colors = get_dominant_colors(image_path, 2)
#     # print(dominant_colors)
#
#     # Open the image
#     img = Image.open(image_path)
#     img = img.convert('RGB')
#
#     # Get image data
#     img_data = np.array(img)
#     # print(img_data)
#
#     # Initialize variables
#     messages = []
#     current_color = None
#     current_message = ""
#     y_start = 0
#
#     # Function to assign speaker based on color
#     def get_speaker(color):
#         return "Speaker_1" if np.array_equal(color, dominant_colors[0]) else "Speaker_2"
#
#     # Scan the image
#     for y in range(img_data.shape[0]):
#         row_colors = defaultdict(int)
#         for x in range(img_data.shape[1]):
#             pixel = tuple(img_data[y, x])
#             row_colors[pixel] += 1
#
#         # Determine the dominant color in this row
#         row_color = max(row_colors, key=row_colors.get)
#
#         # Check if we've switched to a new color
#         if current_color is None or not np.array_equal(row_color, current_color):
#             # If we have a current message, add it to the list
#             if current_color is not None:
#                 messages.append((get_speaker(current_color), (y_start, y), current_message))
#
#             # Start a new message
#             current_color = row_color
#             y_start = y
#             current_message = f"Message starting at y={y}"
#         else:
#             # Continue the current message
#             current_message += f"\nRow at y={y}"
#
#     # Add the last message
#     if current_color is not None:
#         messages.append((get_speaker(current_color), (y_start, img_data.shape[0]), current_message))
#
#     return messages
#
#
# # Usage
# image_path = '/Users/apple/Desktop/nima yozi/rasm.jpg'
# classified_messages = classify_messages(image_path)
#
# for speaker, (start, end), message, current_message in classified_messages:
#     # print(f"{speaker} ({start}-{end}):")
#     # print("Meesage", message)
#     print("Tugadi")