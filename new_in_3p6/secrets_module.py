import secrets

print(secrets.randbelow(100000))
print(secrets.randbits(10))
print(secrets.choice(['a', 'e', 'i', 'o', 'u', 'sometimes y']))
print(secrets.token_bytes(nbytes=100))
print(secrets.token_hex(nbytes=100))
print(secrets.token_urlsafe(nbytes=100))

a = secrets.token_bytes(nbytes=10)
b = secrets.token_bytes(nbytes=10)

# Return True if strings a and b are equal, otherwise False,
# in such a way as to reduce the risk of timing attacks.
print(secrets.compare_digest(a, b))


def xkcd_password(number_of_words: int = 4) -> str:
    """
    Makes a multiple-words, human friendly password as advised by XKCD.
    eg: 'correct horse battery staple'
    Assumes linux with dict words available.
    :param number_of_words: number of words in password.
    :return: the password as a string
    """
    with open('/usr/share/dict/words') as f:
        words = [word.strip() for word in f]
        password = ' '.join(secrets.choice(words) for i in range(number_of_words))
    return password


print(xkcd_password())
print(xkcd_password(number_of_words=6))
