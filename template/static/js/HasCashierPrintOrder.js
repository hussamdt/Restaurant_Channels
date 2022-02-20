var total_price = 0
x = document.getElementsByClassName("custom_price")

Array.prototype.forEach.call(x, function(el) {
    // Do stuff here
    total_price = parseInt(el.innerHTML) + parseInt(total_price)
});

document.getElementById('grand_total').innerHTML = total_price