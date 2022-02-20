const chatSocket = new ReconnectingWebSocket(
    'ws://'
    + window.location.host
    + '/ws/chat/'
    + 'delvery/'
);
function myFunction(){
    chatSocket.onclose = function(e) {
        console.error('Chat socket closed unexpectedly');
    }; 
    chatSocket.send(JSON.stringify({
        'message': 'neworder'
    }));    
}