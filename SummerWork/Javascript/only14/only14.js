/**
 * @param {number[]} nums
 */
function only14(nums) {
  for (const num of nums) {
    if (num !== 1 && num !== 4) {
      return false;
    }
  }
  return true;
}
