/* TODO: Flesh this out to connect the form to the API and render results
   in the #address-results div. */

// Adding event listeners
   document.addEventListener("DOMContentLoaded", function () {
    var form = document.getElementById("address-form");
  
    form.addEventListener("submit", async function (e) {
      e.preventDefault();
    
    //   Declaring variables
      var address = document.getElementById("address").value;
      var url = "/api/parse/";
      var queryParams = new URLSearchParams({ address: address });
  
      try {
        var response = await fetch(`${url}?${queryParams}`, {
          method: 'GET'
        });
  
        var contentData = await response.json();
  
        if (!response.ok) {
          throw new Error(contentData.detail || contentData.error);
        }
  
        displayResults(contentData);
      } catch (error) {
        displayError(error.message);
      }
    });
  
    function displayResults(data) {
      document.getElementById("error-results").style.display = "none";
      var resultsDiv = document.getElementById("address-results");
      resultsDiv.style.display = "block";
  
      document.getElementById("parse-type").textContent = data.address_type;
  
      var tableBody = document.querySelector("#address-results-table tbody");
      tableBody.innerHTML = '';
    
    // Creating table
      for (var [key, value] of Object.entries(data.address_components)) {
        var row = document.createElement("tr");
        var partCell = document.createElement("td");
        var tagCell = document.createElement("td");
  
        partCell.textContent = key;
        tagCell.textContent = value;
  
        row.appendChild(partCell);
        row.appendChild(tagCell);

        tableBody.appendChild(row);
      }
    }
  
    function displayError(errorMessage) {
      document.getElementById("address-results").style.display = "none";

      var errorDiv = document.getElementById("error-results");
      errorDiv.style.display = "block";
      
      document.getElementById("parse-error").textContent = errorMessage;
    }
  });
  