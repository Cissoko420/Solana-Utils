import csv

def extract_txhash_from_csv(csv_file_path, output_file_path):
    with open(csv_file_path, 'r') as csv_file:
        reader = csv.DictReader(csv_file, skipinitialspace=True)
        txhash_list = [row['Txhash'] for row in reader]

    with open(output_file_path, 'w') as output_file:
        for txhash in txhash_list:
            output_file.write(f"{txhash}\n")

csv_file_path = 'INPUT.csv'  # Replace with the actual path to your CSV file
output_file_path = 'out_1.txt'  # Replace with the desired output file path

extract_txhash_from_csv(csv_file_path, output_file_path)
