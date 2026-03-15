from solution import Fancy

def test():
    fancy = Fancy()
    results = [None]
    
    # append(2)
    fancy.append(2)
    results.append(None)
    
    # addAll(3)
    fancy.addAll(3)
    results.append(None)
    
    # append(7)
    fancy.append(7)
    results.append(None)
    
    # multAll(2)
    fancy.multAll(2)
    results.append(None)
    
    # getIndex(0)
    results.append(fancy.getIndex(0))
    
    # addAll(3)
    fancy.addAll(3)
    results.append(None)
    
    # append(10)
    fancy.append(10)
    results.append(None)
    
    # multAll(2)
    fancy.multAll(2)
    results.append(None)
    
    # getIndex(0)
    results.append(fancy.getIndex(0))
    
    # getIndex(1)
    results.append(fancy.getIndex(1))
    
    # getIndex(2)
    results.append(fancy.getIndex(2))
    
    expected = [None, None, None, None, None, 10, None, None, None, 26, 34, 20]
    print(f"Results:  {results}")
    print(f"Expected: {expected}")
    assert results == expected
    print("Test passed!")

if __name__ == "__main__":
    test()
