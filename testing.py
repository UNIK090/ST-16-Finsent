from text import TextToNum # type: ignore

# Test the TextToNum class with a sample input
if __name__ == "__main__":
    test_text = "coding is good, but hard to learn!!"
    ob = TextToNum(test_text)
    ob.cleaner()
    ob.token()
    ob.removeStop()
    dt = ob.stemme()
    print("Processed Text:", dt)
