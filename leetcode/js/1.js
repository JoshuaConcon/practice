/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
  let dictionary = {};
  let result;
  nums.forEach((num, index) => {
    let complementNum = target - num
    if(complementNum in dictionary) {
      result = [index, dictionary[complementNum]]
    }
    dictionary[num] = index
  });
  return result
};