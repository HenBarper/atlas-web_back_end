const Utils = {
  calculateNumber(type, a, b) {
    const firstNum = Math.round(a);
    const secondNum = Math.round(b);

    switch (type) {
      case 'SUM':
        return firstNum + secondNum;
      case 'SUBTRACT':
        return firstNum - secondNum;
      case 'DIVIDE':
        if (secondNum === 0) {
          return 'Error';
        }
        return firstNum / secondNum;
      default:
        throw new Error('Unknown operation');
    }
  }
};
  
module.exports = Utils;