// display vertical nav bar for small screens
function displayNav() {
  var x = document.getElementById("nav__links");
  if (x.classList.contains("responsive")) {
    x.classList.remove("responsive");
  } else {
    x.classList.add("responsive");
  }
}

// display year for copyright 
function getYear() {
  document.write(new Date().getFullYear());
}

//set links to active 
function setToActive(page) {
  link = document.getElementById(page)
  link.classList.add("active")
}