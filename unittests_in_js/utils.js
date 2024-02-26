const Utils = {
  calculateNumber(type, a, b) {
    const firstNum = Math.round(a);
    const secondNum = Math.round(b);

    switch (type) {
      case 'SUM':
        return firstNum + secondNum;
      case 'SUBTRACT':
        return a - secondNum;
      case 'DIVIDE':
        if (numB === 0) {
          return 'Error';
        }
        return numA / numB;
      default:
        throw new Error('Unknown operation');
    }
  }
};
  
module.exports = Utils;