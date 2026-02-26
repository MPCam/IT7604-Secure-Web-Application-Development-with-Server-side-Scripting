const standardShippingCost = 6;
const discountedShippingCost = 4;
let totalPrice;

function calculateShippingCost(totalPriceParam) {
    let shippingCost;

    if (totalPriceParam <= 10) {
        shippingCost = standardShippingCost
    } else if ( totalPriceParam <= 20) {
        shippingCost = discountedShippingCost
    } else {
        shippingCost = 0
    }

    console.log(`Shipping cost for you is $${shippingCost}`);
    console.log(`for total price of $${totalPriceParam}`);
    console.log("----------------");
    
    
}

totalPrice = 10
calculateShippingCost(totalPrice)

totalPrice = 19
calculateShippingCost(totalPrice)

totalPrice = 24
calculateShippingCost(totalPrice)

