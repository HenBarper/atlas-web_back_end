const calculateNumber = require('./1-calcul');
const expect = require('chai');


describe('calculateNumber', () => {
  describe('SUM', () => {
    it('should return rounded sum for SUM', function() {
      expect.strictEqual(calculateNumber('SUM', 6.2, 11.8)).to.equal(18);
    });
  });
  describe('SUBTRACT', () => {
    it('should return rounded difference for SUBTRACT', function() {
        expect.strictEqual(calculateNumber('SUBTRACT', 15.8, 6.2)).to.equal(10);
    });
  });
  describe('DIVIDE', () => {
    it('should return rounded division for DIVIDE', function() {
        expect.strictEqual(calculateNumber('DIVIDE', 9.3, 2.7)).to.equal(3);
    });
    it('should return Error for DIVIDE when b is 0', function() {
        expect.strictEqual(calculateNumber('DIVIDE', 56.9, 0)).to.equal('Error');
    });
  });
});