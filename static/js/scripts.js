/*!
    * Start Bootstrap - SB Admin v7.0.4 (https://startbootstrap.com/template/sb-admin)
    * Copyright 2013-2021 Start Bootstrap
    * Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-sb-admin/blob/master/LICENSE)
    */
    // 
// Scripts
// 

window.addEventListener('DOMContentLoaded', event => {

    // Toggle the side navigation
    const sidebarToggle = document.body.querySelector('#sidebarToggle');
    if (sidebarToggle) {
        // Uncomment Below to persist sidebar toggle between refreshes
        // if (localStorage.getItem('sb|sidebar-toggle') === 'true') {
        //     document.body.classList.toggle('sb-sidenav-toggled');
        // }
        sidebarToggle.addEventListener('click', event => {
            event.preventDefault();
            document.body.classList.toggle('sb-sidenav-toggled');
            localStorage.setItem('sb|sidebar-toggle', document.body.classList.contains('sb-sidenav-toggled'));

        });
    }



});

// 상단 이동 버튼
$(document).ready(function() {
  $('.go-top').hide(0)

  $(window).scroll(function(){
    if($(this).scrollTop() > 100){
      $('.go-top').fadeIn(200);
    } else {
      $('.go-top').fadeOut(300);
    }
  });
  $('.go-top').click(function() {
    event.preventDefault();

    $('html , body').animate({scrollTop: 0}, 10);
  });
});


// 폰트 사이즈 조절 버튼
function changeFont() {
   document.getElementById('demo').style.fontSize='50px';
   }

function downFont() {
   document.getElementById('demo').style.fontSize='15px';
   }


// 복사 버튼
function copyToClipboard(element) {
  var $temp = $("<input>");
  $("body").append($temp);
  $temp.val($(element).text()).select();
  document.execCommand("copy");
  $temp.remove();
}


// 일정 날짜 버튼
function date_cha(val) {
            var today = new Date()
            today.setDate(today.getDate() - val)
            document.getElementById('date1').valueAsDate = today
        }
