let tempp = new TimelineMax({paused:true});
let kempp = new TimelineMax({paused:true});



var clc = document.querySelector('.barbutton');
var cclc = document.querySelector('.navclose');
var k1 = document.querySelector('.but1');
var k2 = document.querySelector('.but2');
var k3 = document.querySelector('.but3');
var k4 = document.querySelector('.but4');
var k5 = document.querySelector('.but5');
var k6 = document.querySelector('.but6');
var k7 = document.querySelector('.but7');
var k8 = document.querySelector('.but8');
var k9 = document.querySelector('.but9');


tempp.addLabel("coress");

tempp
    .set('.clubt',{css:{display:"none"}})
    .to('.mynewnavbar',1,{x:0 ,ease: Sine.easeOut},"coress")
    .to('.webbody',0.2,{opacity:0.4},"coress")
    .set('.upevents',{css:{display:"none"}})
    .set('#social-links',{css:{opacity:0}})
    .set('body',{css:{overflow:"hidden"}})

kempp
    .to('.mynewnavbar',1.8,{x:-1000 ,ease: Sine.easeOut})

clc.onclick = function() {
  tempp.play();
}

cclc.onclick = function() {
  tempp.reverse();
}

k1.onclick = function() {
  tempp.reverse();

}
k2.onclick = function() {
  tempp.reverse();

}
k3.onclick = function() {
  tempp.reverse();

}
k4.onclick = function() {
  tempp.reverse();

}
k5.onclick = function() {
  tempp.reverse();

}
k6.onclick = function() {
  tempp.reverse();

}
k7.onclick = function() {
  tempp.reverse();

}
k8.onclick = function() {
  tempp.reverse();

}
k9.onclick = function() {
  tempp.reverse();

}

let ntemp = new TimelineMax({paused:true});
let stemp = new TimelineMax({paused:true});


stemp
    .to('.icon-bar',0.5,{x:-100})


ntemp
      .to('.clubt',1,{x:500})
      .set('.clubt',{css:{display:"none"}})


window.addEventListener('scroll',()=>{


  if (document.documentElement.scrollTop > 550 ) {
    ntemp.play();
    stemp.reverse();

}
else {
  ntemp.reverse();
  stemp.play();
}
});



let btemp = new TimelineMax({paused:true});

btemp
      .set('.upevents',{css:{opacity:1}})




const utemp = new TimelineMax({paused:true});
var ubutt = document.querySelector('.upevents');
var cbut = document.querySelector('.upclose');

utemp
    .set('.webbody',{css:{display:"none"}})
    .set('.navcolor',{css:{display:"none"}})
    .set('.upevents',{css:{display:"none"}})
    .set('.upcoming',{css:{display:"grid"}})
    .set('.upcoming',{css:{opacity:0}})
    .to('.upcoming',0.8,{ease: Sine.easeOut,opacity:1})
    .set('.upclose',{css:{display:"grid"}})




ubutt.onclick = function() {
  utemp.play();
}

cbut.onclick = function() {
  utemp.reverse();
}
