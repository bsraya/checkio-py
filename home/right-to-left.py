def right_to_left(sentence: tuple) -> str:
    sentence = ','.join(sentence).replace('right', 'left')
    return  

# lambda function
# right_to_left = lambda sentence: ','.join(sentence).replace('right', 'left')


sentence = ("left", "right", "left", "stop")

print(right_to_left(sentence))