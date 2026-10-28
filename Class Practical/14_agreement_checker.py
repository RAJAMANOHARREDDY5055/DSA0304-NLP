
singular_subjects = {"he", "she", "it", "the boy", "the girl", "the cat"}
plural_subjects = {"they", "we", "you", "the boys", "the girls", "the cats"}
singular_verbs = {"runs", "eats", "sleeps", "likes"}
plural_verbs = {"run", "eat", "sleep", "like"}

sentence = input("Enter a simple sentence (example: the cat sleeps): ").lower().strip()
parts = sentence.split()

if len(parts) < 2:
    print("Please enter a subject and a verb.")
else:
    verb = parts[-1]
    subject = " ".join(parts[:-1])
    if subject in singular_subjects and verb in singular_verbs:
        print("Agreement correct (singular subject + singular verb).")
    elif subject in plural_subjects and verb in plural_verbs:
        print("Agreement correct (plural subject + plural verb).")
    else:
        print("Agreement incorrect or sentence not covered by this simple grammar.")
