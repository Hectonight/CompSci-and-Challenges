/**
 * @param {number} temp1
 * @param {number} temp2
 */
function icyHot(temp1, temp2) {
  return (temp1 > 100 && temp2 < 0) || (temp1 < 0 && temp2 > 100);
}
