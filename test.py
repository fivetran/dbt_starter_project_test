# test.py

# Dummy secret for testing purposes only
FAKE_SECRET = "sk_test_1234567890abcdef"
PASSWORD = "Can we confused truffle"

def get_secret():
    return FAKE_SECRET

if __name__ == "__main__":
    print("The fake secret is:", get_secret())