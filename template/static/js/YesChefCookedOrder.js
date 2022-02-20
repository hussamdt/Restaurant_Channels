const chatSocket = new ReconnectingWebSocket(
    'ws://'
    + window.location.host
    + '/ws/chat/'
    + 'chief/'
);

chatSocket.onmessage = function(e) {
    location.href = location.href+'#neworder';
};

chatSocket.onclose = function(e) {
    console.error('Chat socket closed unexpectedly');
};

function locationHashChanged() {
    document.getElementById('notifcation').play();

    location.reload()


}
  
window.onhashchange = locationHashChanged;

