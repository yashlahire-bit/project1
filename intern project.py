import zxcvbn
import itertools

def analyze_password(password): 
    results = zxcvbn.zxcvbn(password)
    print(f"\n--- Analysis for: {password} ---")
    print(f"Score: {results['score']}/4") 
    print(f"Estimated Crack Time: {results['crack_times_display']['offline_fast_hashing_1e10_per_second']}")
    if results['feedback']['suggestions']:
        print(f"Suggestions: {', '.join(results['feedback']['suggestions'])}")

def generate_wordlist(base_words):
    leetspeak_map = {'a': '@', 'e': '3', 'i': '1', 'o': '0', 's': '$'}
    wordlist = []
    
    for word in base_words:
        wordlist.append(word)
        wordlist.append(word + "2024")
        wordlist.append(word + "2025")
         
        leet_word = "".join(leetspeak_map.get(char, char) for char in word.lower())
        wordlist.append(leet_word)
        
    with open("custom_wordlist.txt", "w") as f:
        for item in set(wordlist):
            f.write(item + "\n")
    print(f"\n[+] Success! {len(set(wordlist))} words saved to custom_wordlist.txt")


if __name__ == "__main__": 
    pwd = input("Enter a password to analyze: ")
    analyze_password(pwd)
    
     
    print("\n--- Wordlist Generator ---")
    inputs = input("Enter keywords (e.g., name, pet, city) separated by commas: ")
    base_data = [i.strip() for i in inputs.split(",")]
    generate_wordlist(base_data)
