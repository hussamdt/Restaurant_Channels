window.onload = function(){ 
    var y = document.getElementsByClassName("mybutton") ;
    for (let i = 0; i < y.length; i++) {
      y[i].onclick = function(e) {
        let prevSibling = y[i].previousElementSibling;
        if (prevSibling.style.display === "none") {
          prevSibling.style.display = "block"
        } else {
          prevSibling.style.display = "none"
        }

      }
      
    }



    var close = document.getElementById("closebtn");
    var i;

    close.onclick = function(){
      var div = this.parentElement;
      div.style.opacity = "0";
      setTimeout(function(){ div.style.display = "none"; }, 600);
    } 

}

var parts = window.location.pathname.split('/');
var lastSegment = parts.pop() || parts.pop();  // handle potential trailing slash
x = document.getElementsByClassName("order_id") ;
for (let i = 0; i < x.length; i++) {
  x[i].value = lastSegment
};