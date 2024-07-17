import re
from collections import Counter

# Function to read the contents of a file
def read_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content

# Function to process the text and count word frequencies
def count_word_frequencies(text):
    # Remove punctuation and convert to lowercase
    text = re.sub(r'[^\w\s]', '', text).lower()
    # Split text into words
    words = text.split()
    # Count the frequency of each word
    word_counts = Counter(words)
    return word_counts

# Function to write the word frequencies to a new file
def write_frequencies_to_file(word_counts, output_file_path):
    with open(output_file_path, 'w') as file:
        for word, count in word_counts.items():
            file.write(f'{word}: {count}\n')

# Main function to execute the program
def main(input_file_path, output_file_path):
    # Read the file
    text = read_file(input_file_path)
    # Count word frequencies
    word_counts = count_word_frequencies(text)
    # Write the frequencies to a new file
    write_frequencies_to_file(word_counts, output_file_path)
    print(f'Word frequencies written to {output_file_path}')

# Example usage
if __name__ == "__main__":
    input_file = 'sample_text.txt'  # Replace with your input file path
    output_file = 'word_frequencies.txt'  # Replace with your desired output file path
    main(input_file, output_file)
