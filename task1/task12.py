def level (text):
    letters = sum(1 for char in text if char.isalpha() )
    words = len(text.split())
    sentences = text.count('.') + text.count('!') + text.count('?')

    letters_per_100_words = (letters / words) * 100
    sentences_per_100_words = (sentences / words) * 100

    index = 0.0588 * letters_per_100_words - 0.296 * sentences_per_100_words - 15.8
    grade_level = round(index)

    if grade_level >= 16:
        return "Grade 16+"
    elif grade_level < 1:
        return "Before Grade 1"
    else:
        return f"Grade {grade_level}"

text = input("Enter the text: ")
grade = level (text)
print(grade)



