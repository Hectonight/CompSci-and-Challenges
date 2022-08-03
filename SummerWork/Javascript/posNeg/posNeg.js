/**
 * @param {number} a
 * @param {number} b
 * @param {boolean} negative
 */
function posNeg(a, b, negative) {
  return negative
    ? Math.sign(a) < 0 && Math.sign(b) < 0
    : Math.sign(a) != Math.sign(b);
}
