#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os

def main():
    # Gather inputs
    title = input("Please enter the title: ")
   
    while not title.strip():
        print("Title cannot be empty. Please enter again.")
        title = input("Please enter the title: ")

    url = input("Please enter the URL: ")
   
    keywords = []
    while True:
        keyword = input("Enter a keyword (leave blank to finish): ")
        if not keyword:
            break
        keywords.append(f"[[{keyword}]]")

    # Create the .md content
    content = f"""
{title}

{url}

{" ".join(keywords)}
"""

    # Path where to save the file
    base_path = "/Users/braydennoh/Documents/paper"
    sanitized_title = title.replace(" ", "_").replace("/", "_")
   
    # Truncate the filename if it's too long
    max_filename_length = 200  # This can be adjusted
    if len(sanitized_title) > max_filename_length:
        sanitized_title = sanitized_title[:max_filename_length]

    filename = sanitized_title + ".md"
    save_path = os.path.join(base_path, filename)
   
    try:
        with open(save_path, 'w') as file:
            file.write(content)
        print(f"File saved successfully at {save_path}")
    except Exception as e:
        print(f"An error occurred while saving the file: {e}")

if __name__ == "__main__":
    main()


# In[ ]:




