/**
 * @param {{ filter: (arg0: (num: number) => boolean) => { (): number; new (): boolean; length: number; }; }} nums
 */
function arrayCount9(nums) {
  return nums.filter((/** @type {number} */ num) => num === 9).length;
}
