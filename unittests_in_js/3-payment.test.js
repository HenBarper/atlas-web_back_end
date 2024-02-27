const expect = require('chai').expect;
const sinon = require('sinon');
const sendPaymentRequestToApi = require('./3-payment');
const Utils = require('./utils');

describe('sendPaymentRequestToApi', function() {
  let sinonSpy;
  afterEach(() => {
    sinonSpy.restore();
  });

  it('two funcs should match', function() {
    sinonSpy = sinon.spy(Utils, 'calculateNumber');
    sendPaymentRequestToApi(100, 20);
    // expect(calculateNumberSpy.calledOnce).to.be.true;
    expect(sinonSpy.calledOnceWithExactly('SUM', 100, 20)).to.be.true;
  });
});

// describe('sendPaymentRequestToApi', function() {
//   it('two funcs should match', function() {
//     let sinonSpy = sinon.spy(Utils, 'calculateNumber');

//     sendPaymentRequestToApi(100, 20);
    
//     expect(sinonSpy.calledOnceWithExactly('SUM', 100, 20)).to.be.true;
//     sinonSpy.restore();
//   });
// });