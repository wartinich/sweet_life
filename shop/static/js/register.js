//burger menu start
const iconMenu = document.querySelector('.burger_menu');
if(iconMenu){
    const burgerBody = document.querySelector('.col-md-12.burger_body');
    iconMenu.addEventListener("click",function(e){
    iconMenu.classList.toggle('active');
    burgerBody.classList.toggle('active');
    });
}
//burger menu end

// modal window start
(function () {
    document.querySelector('.popup').classList.toggle ('active')
    document.querySelector("body").classList.toggle('lock');
}());

document.querySelector('.button_x').addEventListener('click',e =>{
    document.querySelector('.popup').classList.toggle ('active');
    document.querySelector("body").classList.toggle('lock');
});
// modal window end