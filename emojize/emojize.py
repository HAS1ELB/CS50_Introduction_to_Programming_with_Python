import emoji

user_answer = input("Input: ")

output = emoji.emojize(user_answer , language = 'alias' )

print("Output:", output)
