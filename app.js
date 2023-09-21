alert("ok");

let tg = window.Telegram.WebApp;

tg.expand();

btn1 = document.getElementById('btn3');
btn2 = document.getElementById('btn4');

btns1 = document.querySelector('.x1');
btns2 = document.querySelector('.x2');
btns3 = document.querySelector('.x3');
btns4 = document.querySelector('.x4');


let cost_from=50000,cost_to=15000000;

$("#slider2").ionRangeSlider({
    type: "double",
    skin:"round",
    min: 50000,
    max: 15000000,
    from: 50000,
    to: 15000000,
    step: 1000,
    postfix: '$',
    hide_min_max: true,
    onFinish: function (data) {
            cost_from=data.from;
            cost_to=data.to;
    },

});


$("#slider1").ionRangeSlider({
    type: "double",
    skin:"round",
    min: 50000,
    max: 1236000,
    from: 50000,
    to: 15000000,
    step: 1000,
    postfix: '$',
    hide_min_max: true,
    onFinish: function (data) {
            cost_from=data.from;
            cost_to=data.to;
    },

});

active = 1;
$(".inner").appendTo($(".container"));
let p = $(".inner2").detach();


function ChangeTo2(){
    active = 1;
    btns1.classList.add("act");
    btns3.classList.add("act");
    btns2.classList.remove("act");
    btns4.classList.remove("act");
    console.log(btn1);
    p.fadeOut(1);
    p.appendTo($(".container"));
    p.fadeIn(1500);
    p = $(".inner2").detach();
    console.log(p);
    console.log(active);
}
function ChangeTo1(){
    active = 2;
    console.log(btn2);
    btns2.classList.add("act");
    btns4.classList.add("act");
    btns1.classList.remove("act");
    btns3.classList.remove("act");
    p.fadeOut(1);
    p.appendTo($(".container"));
    p.fadeIn(1500);
    p = $(".inner").detach();
    console.log(p);
    console.log(active);
}


function SendData(){
    let data='';
    if (active==1)
    {
        data+='new_building ';
        data+=cost_from+' '+cost_to+' ';
        if (document.getElementById("el1").checked==1) data+='Rostov ';
        if (document.getElementById("el5").checked==1) data+='apartment ';
        if (document.getElementById("el2").checked==1) data+='townhouse ';
        if (document.getElementById("el6").checked==1) data+='villa ';
        if (document.getElementById("el7").checked==1) data+='studio ';
        if (document.getElementById("el8").checked==1) data+='1+1 ';
        if (document.getElementById("el9").checked==1) data+='2+1 ';
        if (document.getElementById("el10").checked==1) data+='3+1 ';
        if (document.getElementById("el11").checked==1) data+='4+1 ';
        if (document.getElementById("el12").checked==1) data+='5+1 ';
        if (document.getElementById("el13").checked==1) data+='6+1 ';
        if (document.getElementById("el13").checked==1) data+='7+1 ';
    } else {
        data+='from_the_owner ';
        data+=cost_from+' '+cost_to+' ';
        if (document.getElementById("ell1").checked==1) data+='Rostov ';
        if (document.getElementById("ell2").checked==1) data+='apartment ';
        if (document.getElementById("ell3").checked==1) data+='villa ';
        if (document.getElementById("ell4").checked==1) data+='1+1 ';
        if (document.getElementById("ell5").checked==1) data+='2+1 ';
        if (document.getElementById("ell6").checked==1) data+='3+1 ';
    }
    console.log(data);
    tg.sendData(data);
}

function G() {
  tg.sendData("show");
}