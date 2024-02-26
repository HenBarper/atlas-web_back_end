const calculateNumber = require('./1-calcul');
const assert = require('assert');

describe('SUM', () => {
  it('should return rounded sum for SUM', function() {
    assert.strictEqual(calculateNumber('SUM', 6.2, 11.8), 18);
  });
  it('should return rounded sum for SUM', function() {
    assert.strictEqual(calculateNumber('SUM', -2.1, 22.4), 20);
  });
  it('should return rounded difference for SUBTRACT', function() {
    assert.strictEqual(calculateNumber('SUBTRACT', 15.8, 6.2), 10);
  });
  it('should return rounded difference for SUBTRACT', function() {
    assert.strictEqual(calculateNumber('SUBTRACT', 5.1, -7.9), -3);
  });
  it('should return rounded division for DIVIDE', function() {
    assert.strictEqual(calculateNumber('DIVIDE', 9.3, 2.7), 3);
  });
  it('should return rounded division for DIVIDE', function() {
    assert.strictEqual(calculateNumber('DIVIDE', 5.8, 3.1), 2);
  });
  it('should return Error for DIVIDE when b is 0', function() {
    assert.strictEqual(calculateNumber('DIVIDE', 56.9, 0), 'Error');
  });
});
describe('SUBTRACT', () => {
  it('should return rounded difference for SUBTRACT', function() {
    assert.strictEqual(calculateNumber('SUBTRACT', 15.8, 6.2), 10);
  });
  it('should return rounded difference for SUBTRACT', function() {
    assert.strictEqual(calculateNumber('SUBTRACT', 5.1, -7.9), -3);
  });
});
describe('DIVIDE', () => {
  it('should return rounded division for DIVIDE', function() {
    assert.strictEqual(calculateNumber('DIVIDE', 9.3, 2.7), 3);
  });
  it('should return rounded division for DIVIDE', function() {
    assert.strictEqual(calculateNumber('DIVIDE', 5.8, 3.1), 2);
  });
  it('should return Error for DIVIDE when b is 0', function() {
    assert.strictEqual(calculateNumber('DIVIDE', 56.9, 0), 'Error');
  });
});