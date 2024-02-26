from collections import Counter
import string

def count_word_frequency(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read().lower()  # Read the file and convert to lowercase
        # Remove punctuation from the text
        text = text.translate(str.maketrans('', '', string.punctuation))
        words = text.split()  # Split the text into words
        word_counts = Counter(words)  # Count the occurrences of each word

    # Print word frequency in descending order
    for word, count in word_counts.most_common():
        print(f'{word}: {count}')

# Replace 'your_text_file.txt' with the path to your actual text file
count_word_frequency('C:/Users/Jai Shree Ram/Desktop/paragraph1.txt')
