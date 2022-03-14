function telephoneCheck(str) {
  const reg = /^(1\s?)?(\(\d{3}\)|\d{3})[\s\-]?\d{3}[\s\-]?\d{4}$/
  // Good luck!
  return reg.test(str);
}

telephoneCheck("555555555");