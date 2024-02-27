const request = require('request');
const expect = require('chai').expect;

describe('Index page', function() {
    // no longer needed
});

describe('Cart page', function () {
    it('200 when id is a number', function (done) {
        request('http://localhost:7865/cart/12', function (error, response, body) {
            expect(response.statusCode).to.equal(200);
            expect(body).to.equal('Payment methods for cart 12');
            done();
        });
    });

    it('404 when id is not a number?', function (done) {
        request('http://localhost:7865/cart/hello', function (error, response, body) {
            expect(response.statusCode).to.equal(404);
            done();
        });
    });
});