/**
 * Created by piyush0 on 14/07/17.
 */

var timer = 0;
var clock = null;
var form = null;
var inpTime = null;
var answer = null;
var time_value = null;


window.onload = function () {
    time_value = document.getElementById("t");
    clock = setInterval(counter, 1000);
    form = document.forms["form"];
    inpTime = document.getElementById("timer");
    answer = document.getElementById("answer");
};

function submission() {
    inpTime.value = timer;
    form.submit();
}


function counter() {
    timer++;
    time_value.innerHTML = "Time: " +timer;
    if (timer == 10) {
        clearInterval(clock);
        inpTime.value = 10;
        answer.value = "z";
        form.submit();
    }
}