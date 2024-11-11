document.addEventListener('DOMContentLoaded', function() {
    // SideNav Initialization
  let sidenav = document.querySelectorAll('.sidenav');
  M.Sidenav.init(sidenav);

});

document.addEventListener('DOMContentLoaded', function() {
  // Tooltips on Passwords
  let tooltipped = document.querySelectorAll('.tooltipped');
  M.Tooltip.init(tooltipped);
});

document.addEventListener('DOMContentLoaded', function() {
  let select = document.querySelectorAll('select');
  M.FormSelect.init(select);
});

setTimeout(function() {
  const flashMessages = document.querySelectorAll('.card-panel-message');
  flashMessages.forEach(msg => msg.style.display = 'none');
}, 5000);