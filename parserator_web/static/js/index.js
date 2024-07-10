/* TODO: Flesh this out to connect the form to the API and render results
   in the #address-results div. */
"use strict";

document.querySelector("form").addEventListener("submit", function (event) {
  event.preventDefault();
  const address = document.querySelector("input[name='address']").value;
  console.log(address);
  fetch(`/api/parse?address=${encodeURIComponent(address)}`)
    .then((response) => response.json())
    .then((data) => {
      const resultsDiv = document.getElementById("address-results");
      if (data.error) {
        resultsDiv.textContent = data.error;
      } else {
        // Display parsed address components in the table
        const tbody = resultsDiv.querySelector("tbody");
        tbody.innerHTML = ""; // Clear previous results
        for (const [key, value] of Object.entries(data.address_components)) {
          const row = document.createElement("tr");
          const partCell = document.createElement("td");
          const tagCell = document.createElement("td");
          partCell.textContent = key;
          tagCell.textContent = value;
          row.appendChild(partCell);
          row.appendChild(tagCell);
          tbody.appendChild(row);
        }
        document.getElementById("parse-type").textContent = data.address_type || "Unknown";
      }
      resultsDiv.style.display = "block";
    })
    .catch((error) => {
      console.error("Error:", error);
    });
});
