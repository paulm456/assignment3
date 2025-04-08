// JavaScript source code
/* When the user clicks on the button, 
toggle between hiding and showing the dropdown content */
function myFunction() {
    document.getElementById("myDropdown").classList.toggle("show");
  }
  
  // Close the dropdown if the user clicks outside of it
  window.onclick = function(event) {
    if (!event.target.matches('.dropbtn')) { // if the target of the click isn't the dropdown close dropdown if open
      var dropdowns = document.getElementsByClassName("dropdown-content");
      var i;
      for (i = 0; i < dropdowns.length; i++) {
        var openDropdown = dropdowns[i];
        if (openDropdown.classList.contains('show')) {
          openDropdown.classList.remove('show');
        }
      }
    }
  }



  // Function for Navigation Dropdown
function toggleNavMenu() {
  document.getElementById("navDropdown").classList.toggle("show-nav");
}

// Close Navigation Dropdown if user clicks outside
window.onclick = function(event) {
  if (!event.target.matches('.nav-menu-btn')) {
      var dropdown = document.getElementById("navDropdown");
      if (dropdown.classList.contains('show-nav')) {
          dropdown.classList.remove('show-nav');
      }
  }
}
  


  