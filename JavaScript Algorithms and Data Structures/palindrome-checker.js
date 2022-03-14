function palindrome(str) {
    const cleanStr = str.replace(/[^a-zA-Z0-9]/g, '').toLowerCase()
    const reverseCleanStr = Array.from(cleanStr).reverse().join('')
    return cleanStr === reverseCleanStr
  }

  palindrome("A man, a plan, a canal. Panama");