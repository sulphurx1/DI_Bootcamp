const stock = { 
    "banana": 6, 
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry":1
}  

const prices = {    
    "banana": 4, 
    "apple": 2, 
    "pear": 1,
    "orange": 1.5,
    "blueberry":10
} 

const shoppingList = [`banana`, `orange`, `apple`]
 
function myBill() {
    
    

    shoppingList.forEach(item => {
        const quantityInStock = stock[item]
        
    if(quantityInStock > 0) {

        const cost = prices[item] // finding price of object
        stock[item] = stock[item] - 1 // reducing stock
        console.log(`The price of `+ item + ` is ` + cost)  
        }
    })
}

myBill()


