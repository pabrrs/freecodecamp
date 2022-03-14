function rot13(str) {
  const alphabeth = Array.from('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
  return Array.from(str)
    .reduce((acc, char) => {
      if (alphabeth.indexOf(char) === -1) return acc.concat(char)
      const index = alphabeth.indexOf(char) + 13
      const rot13Index = index >= alphabeth.length ?
        index - alphabeth.length :
        index
      return acc.concat(alphabeth[rot13Index])
    }, '')
}

rot13("SERR PBQR PNZC")