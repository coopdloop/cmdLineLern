function update(){

    var v = document.getElementById('uinput').value;
    var url = "/user_input" + "?user_input_field=" + v;
    
    var req = new XMLHttpRequest();
    req.open("GET", url, false);
    req.send();

    //alert(req.responseText);
    document.getElementById('termWindow').value = req.responseText;



}