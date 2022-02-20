const chatSocket = new ReconnectingWebSocket(
    'ws://'
    + window.location.host
    + '/ws/chat/'
    + 'order/'
);

chatSocket.onmessage = function(e) {
    location.href = location.href+'#neworder';

};

chatSocket.onclose = function(e) {
    console.error('Chat socket closed unexpectedly');
    
};


const chatSocket2 = new ReconnectingWebSocket(
    'ws://'
    + window.location.host
    + '/ws/chat/'
    + 'delvery/'
);

chatSocket2.onmessage = function(e) {
    location.href = location.href+'#neworder';
};

chatSocket2.onclose = function(e) {
    console.error('Chat socket closed unexpectedly');
};




function locationHashChanged() {
    document.getElementById('notifcation').play();

    location.reload()

}
  
window.onhashchange = locationHashChanged;