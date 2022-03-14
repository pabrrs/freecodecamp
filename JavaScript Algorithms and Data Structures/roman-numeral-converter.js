function convertToRoman(num) {

  const romanMapping = [
    { arabian: 1000, roman: 'M' },
    { arabian: 900, roman: 'CM' },
    { arabian: 500, roman: 'D' },
    { arabian: 400, roman: 'CD' },
    { arabian: 100, roman: 'C' },
    { arabian: 90, roman: 'XC' },
    { arabian: 50, roman: 'L' },
    { arabian: 40, roman: 'XL' },
    { arabian: 10, roman: 'X' },
    { arabian: 9, roman: 'IX' },
    { arabian: 5, roman: 'V' },
    { arabian: 4, roman: 'IV' },
    { arabian: 1, roman: 'I' }
  ]
  
  let romanNum = ''
  let remainNum = num

  while (remainNum != 0) {
    const nearestRoman = romanMapping.find(n => remainNum / n.arabian >= 1)
    console.log(remainNum, nearestRoman)
    if (!!nearestRoman) {
      remainNum = remainNum - nearestRoman.arabian
      romanNum = romanNum.concat(nearestRoman.roman)
    }
  }
  return romanNum
}