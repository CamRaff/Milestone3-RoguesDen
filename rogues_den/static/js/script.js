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
  // Select dropdown
  let select = document.querySelectorAll('select');
  M.FormSelect.init(select);
});

setTimeout(function() {
  // Flash Message initialization
  const flashMessages = document.querySelectorAll('.card-panel-message');
  flashMessages.forEach(msg => msg.style.display = 'none');
}, 5000);

document.addEventListener('DOMContentLoaded', function() {
  // Modal functionality
  let modal = document.querySelectorAll('.modal');
  M.Modal.init(modal);
});

// Function to change input labels on add character page for smaller screens
function changeLabels() {
  const strlab = document.getElementById("strlab");
  const intlab = document.getElementById("intlab");
  const dexlab = document.getElementById("dexlab");
  const conlab = document.getElementById("conlab");
  const wislab = document.getElementById("wislab");
  const chalab = document.getElementById("chalab");

  if (window.innerWidth > 600) {
    strlab.innerHTML = "Strength";
    intlab.innerHTML = "Intelligence";
    dexlab.innerHTML = "Dexterity";
    conlab.innerHTML = "Constitution";
    wislab.innerHTML = "Wisdom";
    chalab.innerHTML = "Charisma";
  } else {
    strlab.innerHTML = "Str";
    intlab.innerHTML = "Int";
    dexlab.innerHTML = "Dex";
    conlab.innerHTML = "Con";
    wislab.innerHTML = "Wis";
    chalab.innerHTML = "Cha";
  }
}
// Run the function when the DOM is ready
document.addEventListener("DOMContentLoaded", changeLabels);
// Run the function when the window is resized
window.addEventListener("resize", changeLabels);

// Functions for changing inner html for stats on view page for smaller screens
function updateStats() {
  const strp = document.getElementById("strength");
  const character_strength = strp.getAttribute("data-strength");
  const dexp = document.getElementById("dexterity");
  const character_dexterity = dexp.getAttribute("data-dexterity");
  const conp = document.getElementById("constitution");
  const character_constitution = conp.getAttribute("data-constitution");
  const intp = document.getElementById("intelligence");
  const character_intelligence = intp.getAttribute("data-intelligence");
  const wisp = document.getElementById("wisdom");
  const character_wisdom = wisp.getAttribute("data-wisdom");
  const chap = document.getElementById("charisma");
  const character_charisma = chap.getAttribute("data-charisma");

  if (window.innerWidth > 600) {
    strp.innerHTML = "Strength:<br>" + character_strength;
    dexp.innerHTML = "Dexterity:<br>" + character_dexterity;
    conp.innerHTML = "Constitution:<br>" + character_constitution;
    intp.innerHTML = "Intelligence:<br>" + character_intelligence;
    wisp.innerHTML = "Wisdom:<br>" + character_wisdom;
    chap.innerHTML = "Charisma:<br>" + character_charisma;
  } else {
    strp.innerHTML = "Str: " + character_strength;
    dexp.innerHTML = "Dex: " + character_dexterity;
    conp.innerHTML = "Con: " + character_constitution;
    intp.innerHTML = "Int: " + character_intelligence;
    wisp.innerHTML = "Wis: " + character_wisdom;
    chap.innerHTML = "Cha: " + character_charisma;
  }
}
// Run the function when the DOM is ready
document.addEventListener("DOMContentLoaded", updateStats);
// Run the function when the window is resized
window.addEventListener("resize", updateStats);