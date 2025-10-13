type A = {
    id: Number;
    name: string;
}

type B = {
    sku: String;
    price: Number;
}

type C = A | B

function printInfo(item: C) {
    if ('id' in item) {
    console.log(`User: ${item.name} (id: ${item.id})`);
  } else {
    console.log(`Product: ${item.sku} - ${item.price}원`);
  }
}

const user: A = {id: 1, name: 'Alice'};
const product: B = {sku:"X123", price:1000};

printInfo(user); //User: Alice (id: 1)
printInfo(product); //Product: X123 - 1000원