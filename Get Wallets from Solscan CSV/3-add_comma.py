def add_comma_to_lines(input_file_path, output_file_path):
    with open(input_file_path, 'r') as input_file:
        lines = [line.strip() + ',' for line in input_file.readlines()]

    with open(output_file_path, 'w') as output_file:
        output_file.write("\n".join(lines))

# Example usage
input_file_path = 'sender_addresses.txt'
output_file_path = 'sender_addresses_comma.txt'

add_comma_to_lines(input_file_path, output_file_path)
