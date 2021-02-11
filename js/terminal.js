function update(){

    var v = document.getElementById('uinput').value;
    var url = "/user_input" + "?user_input_field=" + v;
    
    var req = new XMLHttpRequest();
    req.open("GET", url, false);
    req.send();

    var url2 = "/pwd" + "?user_input_field=" + v;
    var req2 = new XMLHttpRequest();
    req2.open("GET", url2, false);
    req2.send();
    //alert(req.responseText);
    terminalWindow = document.getElementById('termWindow');
    terminalWindowText = document.getElementById('termWindow').value;
    terminalWindow.scrollTop = terminalWindow.scrollHeight;


    terminalWindowText = terminalWindowText + "\nUser1@cmdLineLern: " + req2.responseText + "# " +v + "\n"+ req.responseText;



}