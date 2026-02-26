let name = "some-name"
console.log(name)
console.log("output in console from app.js files")


let totalPrice = 19;
let shippingCost;

if (totalPrice >= 20) {
    shippingCost = 0
} else {
    shippingCost = 5
}

console.log(shippingCost)


if (totalPrice <= 10) {
    shippingCost = 5
} else if (totalPrice <= 20) {
    shippingCost = 3
} else {
    shippingCost = 0
}

console.log(shippingCost)


let userMembership;

if (userMembership !== 'premium') {
    // show non premium content
    // or upgrade option
} else {
    // show premium content
}


// todayDate === birthdayDate AND birthdayDisplayed === true
let todayDate;
let birthdayDate;
let birthdayDisplayed;

if (todayDate === birthdayDate && birthdayDisplayed === true) {
    // show notification
} else {
    // do not
}


let amazonPrice;
let amazonPrime;

// only one needs to be true
if (totalPrice > 20 || amazonPrice === true) {
    // free shipment
} else {
    // no free shipment
}



// negation, checking if full condition is false
if (!(totalPrice > 20 || amazonPrice === true)) {
    // free shipment
} else {
    // no free shipment
}