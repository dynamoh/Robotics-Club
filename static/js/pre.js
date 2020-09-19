
const home  = new TimelineMax();
home
.to('.navButton-text',0.2,{text:"About Us"});
// .to("#home-btn",1,{opacity:0,text:"maman"});
const about  = new TimelineMax();
about
.to(".navButton-text",0.2,{text:"Projects"});
const projects  = new TimelineMax();
projects
.to(".navButton-text",0.2,{text:"Schedule"});
const teams  = new TimelineMax();
teams
.to(".navButton-text",0.2,{text:"Achievements"});
const gallery  = new TimelineMax();
gallery
.to(".navButton-text",0.2,{text:"Team"});
const contact  = new TimelineMax();
contact
.to(".navButton-text",0.2,{text:"Gallery"});
const sponsors  = new TimelineMax();
sponsors
.to(".navButton-text",0.2,{text:"Contact Us"});




 const controller = new ScrollMagic.Controller();

 const scene1 = new ScrollMagic.Scene({
    trigger:"#aboutiitr",
    offset:555,
    duration:50,
    reverse:true,
    triggerHook:0.5,
})
.setTween(home)

.addTo(controller);

const scene2 = new ScrollMagic.Scene({
    trigger:"#project-section",
    offset:1450,
    duration:50,
    reverse:true,
    triggerHook:0.5,
})
.setTween(about)

.addTo(controller);

const scene3 = new ScrollMagic.Scene({
    trigger:"#schedule-section",
    offset:2320,
    duration:50,
    reverse:true,
    triggerHook:0.5,
})
.setTween(projects)

.addTo(controller);

const scene4 = new ScrollMagic.Scene({
    trigger:"#achievement-section",
    offset:3060,
    duration:50,
    reverse:true,
    triggerHook:0.5,
})
.setTween(teams)

.addTo(controller);

const scene6 = new ScrollMagic.Scene({
    trigger:"#ourteam-section",
    offset:3900,
    duration:50,
    reverse:true,
    triggerHook:0.5,
})
.setTween(gallery)

.addTo(controller);

const scene7 = new ScrollMagic.Scene({
    trigger:"#gallery-section",
    offset:4600,
    duration:50,
    reverse:true,
    triggerHook:0.5,
})
.setTween(contact)

.addTo(controller);

const scene8 = new ScrollMagic.Scene({
    trigger:"#contact-section",
    offset:5300,
    duration:50,
    reverse:true,
    triggerHook:0.5,
})
.setTween(sponsors)

.addTo(controller);
