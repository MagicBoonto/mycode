#!/usr/bin/env python3

# Define two lists for breakfast foods
breakfast = ["cereal", "toast", "eggs"]
breakfast_copy = ["cereal", "toast", "eggs"]  # Create a copy of the original list

# Print the original list of breakfast foods
print("Original breakfast list:")
print(breakfast)

# Append "pancakes" to the end of both lists
breakfast.append("pancakes") 
breakfast_copy.append("pancakes")

# Print the lists after appending "pancakes"
print("\nBreakfast list after adding pancakes:")
print(breakfast)
print("Copy of breakfast list after adding pancakes:")
print(breakfast_copy)

# Define a new list 'fruits' containing fruits commonly eaten for breakfast
fruits = ["banana", "apple", "orange"]

# Extend the 'breakfast' list by adding the elements of 'fruits' to it
breakfast.extend(fruits)

# Append the 'fruits' list itself to the 'breakfast_copy' list
breakfast_copy.append(fruits)

# Print the lists after extending 'breakfast' and appending 'fruits' to 'breakfast_copy'
print("\nBreakfast list after extending with fruits:")
print(breakfast)
print("Copy of breakfast list after appending fruits list:")
print(breakfast_copy)

# Reverse the 'breakfast' list in place
breakfast.reverse()

# Print the reversed 'breakfast' list
print("\nReversed breakfast list:")
print(breakfast)

