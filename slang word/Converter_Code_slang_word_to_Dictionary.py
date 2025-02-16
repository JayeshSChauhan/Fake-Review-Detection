def txt_to_dict(input_file, output_file):
    # Read the content from the input txt file
    with open(input_file, 'r') as file:
        lines = file.readlines()

    # Initialize an empty dictionary
    content_dict = {}

    # Process each line in the file
    for line in lines:
        # Split each line into key-value pair assuming ':' separates the key and value
        if ':' in line:
            key, value = line.strip().split(':', 1)
            content_dict[key.strip()] = value.strip()

    # Format the dictionary content and write to the output txt file
    with open(output_file, 'w') as file:
        for key, value in content_dict.items():
            file.write(f'"{key}": "{value}",\n')

    return content_dict

# Example usage:
input_file = 'slang_words.txt'  # Your input text file
output_file = 'slang_words_dictionary_form.txt'  # Your output text file

result_dict = txt_to_dict(input_file, output_file)
print(f'Dictionary content from the file: {result_dict}')
