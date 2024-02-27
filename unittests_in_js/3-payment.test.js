const expect = require('chai').expect;
const sinon = require('sinon');
const sendPaymentRequestToApi = require('./3-payment');
const Utils = require('./utils');

describe('sendPaymentRequestToApi', function() {
    it('two funcs should match', function() {
        let sinonSpy = sinon.spy(100, 20);
        let utilsSum = Utils.calculateNumber('SUM', 100, 20);
        sendPaymentRequestToApi(sinonSpy);
        expect(sinonSpy).to.equal(utilsSum);
    });
});