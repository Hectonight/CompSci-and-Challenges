// This function will assume all array lengths are even
/**
 * @param {number[]} nums
 */
function makeMiddle(nums) {
  return nums.slice(nums.length / 2 - 1, nums.length / 2 + 1);
}
