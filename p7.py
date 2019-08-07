def palindrome(input):
    length = len(input)
    palindromes = []
    for x in range(2,len(input)+1):
        min = 0
        while (min+x) < length+1:
            if(input[min:(min+x)] == input[min:(min+x)][::-1]):
                palindromes.append(input[min:(min+x)])
            min = min+1
    for i in palindromes:
      print(i)
  
n=input()
palindrome(n)
