function validateBooking() {

    // Retrieve form data
    let bookingType = document.getElementById("type").value.trim();
    let payment = document.getElementById("pay").value.trim();
    let checkIn = document.getElementById("checkin").value;
    let checkOut = document.getElementById("checkout").value;
    let guests = document.getElementById("guests").value.trim();

    if (!bookingType || !payment || !checkIn || !checkOut || !guests) {
        alert("Please fill in all required fields.");
        return false;
    }

    // Create a new booking object
    let booking = {
        type: bookingType,
        checkIn: checkIn,
        checkOut: checkOut
    };

    // Retrieve existing bookings from localStorage or initialize an empty array
    let bookings = JSON.parse(localStorage.getItem("bookings")) || [];

    // Add new booking to the array
    bookings.push(booking);

    // Save updated bookings array back to localStorage
    localStorage.setItem("bookings", JSON.stringify(bookings));

    // Refresh table to show new booking
    loadBookings();

    // Clear the form fields after submission
    document.getElementById("bookingForm").reset();

    return false;
}

// Function to load bookings from localStorage on page load
function loadBookings() {
    let tableBody = document.querySelector("#bookingTable tbody");
    tableBody.innerHTML = ""; // Clear existing table data

    // Retrieve bookings from localStorage or initialize an empty array
    let bookings = JSON.parse(localStorage.getItem("bookings")) || [];

    // Loop through each booking and add it to the table
    bookings.forEach(booking => {
        let newRow = tableBody.insertRow();

        let typeCell = newRow.insertCell(0);
        let checkInCell = newRow.insertCell(1);
        let checkOutCell = newRow.insertCell(2);

        typeCell.textContent = booking.type;
        checkInCell.textContent = booking.checkIn;
        checkOutCell.textContent = booking.checkOut;
    });
}

// Load bookings when the page is loaded
document.addEventListener("DOMContentLoaded", loadBookings);
