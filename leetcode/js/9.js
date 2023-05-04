/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
  const xStr = x.toString();
  let leftPtrIndex = 0;
  let rightPtrIndex = xStr.length - 1;
  while(leftPtrIndex < rightPtrIndex) {
    if(xStr[leftPtrIndex] !== xStr[rightPtrIndex]) {
      return false
    }
    leftPtrIndex++;
    rightPtrIndex--;
  };
  return true;
};