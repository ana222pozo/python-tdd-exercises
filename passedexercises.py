### TESTS PASSED + ADDITIONAL TEST ###


def reverse_list(l):
    """
    Reverses order of elements in list l.
    """
    return l[::-1]


def test_reverse_list():
    assert reverse_list([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]

 
# ------------------------------------------------------------------------------

def reverse_string(s):
    """
    Reverses order of characters in string s.
    """
    return s[::-1]
    


def test_reverse_string():
    assert reverse_string("foobar") == "raboof"

 

# ------------------------------------------------------------------------------

def is_english_vowel(c):
    """
    Returns True if c is an english vowel
    and False otherwise.
    """
    if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u' or c == 'y' or c == 'Y' or c == 'A' or c == 'E' or c == 'I' or c == 'O' or c == 'U':
    	return True
    else:
	return False


def test_is_english_vowel():
    assert is_english_vowel('a')
    assert is_english_vowel('e')
    assert is_english_vowel('i')
    assert is_english_vowel('o')
    assert is_english_vowel('u')
    assert is_english_vowel('y')
    assert is_english_vowel('A')
    assert is_english_vowel('E')
    assert is_english_vowel('I')
    assert is_english_vowel('O')
    assert is_english_vowel('U')
    assert is_english_vowel('Y')
    assert not is_english_vowel('k')
    assert not is_english_vowel('z')
    assert not is_english_vowel('?')

 

# ------------------------------------------------------------------------------

def count_num_vowels(s):
    """
    Returns the number of vowels in a string s.
    """
    x = s.count('a') + s.count('e') + s.count('i') + s.count('o') + s.count('u') + s.count('y') + s.count('A') + s.count('E') + s.count('I') + s.count('O') + s.count('U') + s.count('Y')
	
    return x

def test_count_num_vowels():
    sentence = "hey ho let's go"
    assert count_num_vowels(sentence) == 5
    sentence = "HEY ho let's GO"
    assert count_num_vowels(sentence) == 5
    paragraph = """She told me her name was Billie Jean,
                   as she caused a scene
                   Then every head turned with eyes
                   that dreamed of being the one
                   Who will dance on the floor in the round"""
    assert count_num_vowels(paragraph) == 54

 

# ------------------------------------------------------------------------------

def get_word_lengths(s):
    """
    Returns a list of integers representing
    the word lengths in string s.
    """
    x = []
    for i in s.split():
    	x.append(len(i))
    return x


def test_get_word_lengths():
    text = "Three tomatoes are walking down the street"
    assert get_word_lengths(text) == [5, 8, 3, 7, 4, 3, 6]

 

# ------------------------------------------------------------------------------

def find_longest_word(s):
    """
    Returns the longest word in string s.
    In case there are several, return the first.
    """
    m = 0
    w = ''
    for i in s.split():
	if len(i) > m:
	    m = len(i)
	    w = i
	else:
	    m = m
	    w = w

    return w

def test_find_longest_word():
    text = "Three tomatoes are walking down the street"
    assert find_longest_word(text) == "tomatoes"
    text = "foo foo1 foo2 foo3"
    assert find_longest_word(text) == "foo1"

 

# ------------------------------------------------------------------------------

def validate_dna(s):
    """
    Return True if the DNA string only contains characters
    a, c, t, or g (lower or uppercase). False otherwise.
    """

    t = s.lower()
    c = t.count('a') + t.count('t') + t.count('g') + t.count('c')
    if len(t) > c:
    	return False
    else:
	return True


def test_validate_dna():
    assert validate_dna('CCGGAAGAGCTTACTTAGccggaagagcttacttag')
    assert not validate_dna('xCCGGAAGAGCTTACTTAGccggaagagcttacttag')
    assert not validate_dna('CCxGGAAGAGCTTACTTAGccggaagagcttacttag')

 

# ------------------------------------------------------------------------------

def base_pair(c):
    """
    Return the corresponding character (lowercase)
    of the base pair. If the base is not recognized,
    return 'unknown'.
    """
    l = c.lower()
    if l == 'a':
    	return 't'
    if l == 't':
    	return 'a'
    if l == 'g':
    	return 'c'
    if l == 'c':
    	return 'g'
    if l != 'a' and l != 't' and l != 'g' and l != 'c':
    	return 'unknown'

def test_base_pair():
    assert base_pair('a') == 't'
    assert base_pair('t') == 'a'
    assert base_pair('c') == 'g'
    assert base_pair('g') == 'c'
    assert base_pair('A') == 't'
    assert base_pair('T') == 'a'
    assert base_pair('C') == 'g'
    assert base_pair('G') == 'c'
    assert base_pair('x') == 'unknown'
    assert base_pair('foo') == 'unknown'

 

# ------------------------------------------------------------------------------

def transcribe_dna_to_rna(s):
    """
    Return string s with each letter T replaced by U.
    Result is always uppercase.
    """
    x = s.upper()

    return x.replace('T', 'U')


def test_transcribe_dna_to_rna():
    dna = 'CCGGAAGAGCTTACTTAGccggaagagcttacttag'
    assert transcribe_dna_to_rna(dna) == 'CCGGAAGAGCUUACUUAGCCGGAAGAGCUUACUUAG'

 

# ------------------------------------------------------------------------------

def get_complement(s):
    """
    Return the DNA complement in uppercase
    (A -> T, T-> A, C -> G, G-> C).
    """
    x = s.upper()
    return x.replace('A', 'N').replace('T', 'A').replace('N', 'T').replace('G','M').replace('C', 'G').replace('M', 'C')


def test_get_complement():
    assert get_complement('CCGGAAGAGCTTACTTAG') == 'GGCCTTCTCGAATGAATC'
    assert get_complement('ccggaagagcttacttag') == 'GGCCTTCTCGAATGAATC'

 

# ------------------------------------------------------------------------------

def get_reverse_complement(s):
    """
    Return the reverse complement of string s
    (complement reversed in order).
    """
    x = s.upper()
    z = x.replace('A', 'N').replace('T', 'A').replace('N', 'T').replace('G','M').replace('C', 'G').replace('M', 'C')

    return z[::-1]


def test_get_reverse_complement():
    assert get_reverse_complement('CCGGAAGAGCTTACTTAG') == 'CTAAGTAAGCTCTTCCGG'
    assert get_reverse_complement('ccggaagagcttacttag') == 'CTAAGTAAGCTCTTCCGG'

 

# ------------------------------------------------------------------------------

def remove_substring(substring, string):
    """
    Returns string with all occurrences of substring removed.
    """
    
    return string.replace(substring, '')


def test_remove_substring():
    assert remove_substring('GAA', 'CCGGAAGAGCTTACTTAG') == 'CCGGAGCTTACTTAG'
    assert remove_substring('CCG', 'CCGGAAGAGCTTACTTAG') == 'GAAGAGCTTACTTAG'
    assert remove_substring('TAG', 'CCGGAAGAGCTTACTTAG') == 'CCGGAAGAGCTTACT'
    assert remove_substring('GAA', 'GAAGAAGAA') == ''

# ------------------------------------------------------------------------------

# Additional test

def pro_count(string):
    
    """
    Returns the number of Pro present in a sequence
    """

    s = string.upper()
    return s.count('P')

def test_pro_count():
    assert pro_count('PACGTYPWP') == 3
    assert pro_count('pacgptypwp') == 4	

 
