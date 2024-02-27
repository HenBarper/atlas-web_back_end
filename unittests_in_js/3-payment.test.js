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
    sinonSpy = sinon.spy('Utils', 'calculateNumber');
    sendPaymentRequestToApi(100, 20);
    // expect(calculateNumberSpy.calledOnce).to.be.true;
    expect(calculateNumberSpy.calledOnceWithExactly('SUM', 100, 20)).to.be.true;
  });
});