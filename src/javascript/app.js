var test = require('unit.js');

/* list of products */

var p1 = {price: 20.5, id: 'toto'}
var p2 = {price: 22.50, id: 'tata'}
var p3 = {price: 10.0, id: 'titi'}

/* business rules */

var buy_one_get_one_free = function(products) {
    var totoCount = 0;
    for (var count in products) {
        var product = products[count];
        if (product.id == 'toto') {
            totoCount++;
        }
    }

    if (totoCount >= 2) {
        return -20;
    } else {
        return 0;
    }
}

var buy_more_than_ten = function(products) {
    var productsCount = products.length;
    var THRESOLD = 10;
    if (productsCount >= THRESOLD) {
        return (productsCount - THRESOLD)*-1;
    } else {
        return 0;
    }
}

/* Checkout object */

var Checkout = function(rules) {
    this.rules = rules;
    this.products = new Array();
}

Checkout.prototype.scan = function(product) {
    this.products.push(product);
}

Checkout.prototype.total = function() {
    var totalCount = this.grand_total();
    // apply all business rules
    for (var count in this.rules) {
        var rule = this.rules[count];
        totalCount+=rule(this.products);
    }
    return totalCount;
}

Checkout.prototype.grand_total = function() {
    var totalCount = 0;
    // count all the products
    for (var count in this.products) {
        var product = this.products[count];
        totalCount += product.price;
    }
    return totalCount;
}

var c = new Checkout([buy_one_get_one_free, buy_more_than_ten]);

c.scan(p1);
c.scan(p1);
c.scan(p2);
c.scan(p3);

describe('Test', function() {
    it('Four products', function () {
        test.value(c.grand_total()).is(73.5);
        test.value(c.total()).is(53.5);
    });
    it('More than ten products', function () {
        c.scan(p1);
        c.scan(p1);
        c.scan(p1);
        c.scan(p1);
        c.scan(p1);
        c.scan(p1);
        c.scan(p1);
        test.value(c.grand_total()).is(217);
        test.value(c.total()).is(196);
    });
    it('Business rule "more than ten"', function() {
        test.value(buy_more_than_ten(new Array(12))).is(-2);
        test.value(buy_more_than_ten(new Array(10))).is(0);
        test.value(buy_more_than_ten(new Array(8))).is(0);
    });
});
