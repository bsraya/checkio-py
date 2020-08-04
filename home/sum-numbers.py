def sum_numbers(sentence: str) -> int:
    total = sum(int(word) for word in sentence.split() if word.isdigit())
    return total

lambda_sum_numbers = lambda sentence: sum(int(word) for word in sentence.split() if word.isdigit())

sentence = 'who is 1st there'
sentencetwo = '5 plus 6 is 11'

print(sum_numbers(sentencetwo))
print(lambda_sum_numbers(sentencetwo))
