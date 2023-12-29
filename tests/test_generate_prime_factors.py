import pytest
from scipts.prime import generate_prime_factors

factors = []
exp=[]

'''
def test_integer():
    """ Step 1: Write a test that asserts when generate_prime_factors is called with a data type
     that is not an integer a ValueError is raised 
    """
    
 #   assert generate_prime_factors(1) != ValueError
'''
def test_one():
    """
    Step 2: Write a test that asserts when generate_prime_factors is called with 1 an empty list is returned
    """

    assert bool(generate_prime_factors(1)) == False
  
def test_two():
    """
    Step 3: Write a test that asserts when generate_prime_factors is called with 2 the list [2] is returned
    """

    assert generate_prime_factors(2) == [2]

def test_3():    
    """
    Step 4: Write a test that asserts when generate_prime_factors is called with 3 the list [3] is returned
    """

    assert generate_prime_factors(3) == [3]

def test_four(): 
    """
    Step 5: Write a test that asserts when generate_prime_factors is called with 4 the list [2,2] is returned
    """
    assert generate_prime_factors(4) == [2, 2]
    
def test_six(): 
    """
    Write a test that asserts when generate_prime_factors is called with 6 the list [2,3] is returned
    """
    assert generate_prime_factors(6) == [2, 3]
    
def test_eight(): 
    """
    Write a test that asserts when generate_prime_factors is called with 8 the list [2, 2, 2] is returned
    """
    assert generate_prime_factors(8) == [2, 2, 2]
    
def test_nine(): 
    """
    Write a test that asserts when generate_prime_factors is called with 4 the list [2,2] is returned
    """
    assert generate_prime_factors(9) == [3, 3]
    

