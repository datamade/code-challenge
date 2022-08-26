/* Connects the form to the API and render results
   in the #address-results div. */

$('.form').on('submit', function (event) {
   // Prevent default form submission behavior
   event.preventDefault();

   var address = getAddress();
   submitAddress(address);
});

function getAddress() {
   return $("#address").val().trim();
}

async function submitAddress(address) {
   var preparedAddress = address.replaceAll(" ", "+");
   try {
      fetch("api/parse?address=" + preparedAddress)
         .then((res) => handleResponse(res));
   } catch (error) {
      writeError("Something went wrong, please try again.");
   }
}

async function handleResponse(response) {
   if (response.ok) {
      response.json().then(jsonData => {
         writeResults(jsonData.address_type, jsonData.address_components);
      });
   } else {
      response.json().then(jsonData => {
         writeError(jsonData.detail);
      });
   }
}

function writeResults(addressType, addressComponents) {
   // Write Address Type text
   $("#parse-type").text(addressType);

   // Write Address Components table
   $("#address-parts").empty();
   for (var component in addressComponents) {
      if (Object.prototype.hasOwnProperty.call(addressComponents, component)) {
         var row = `<tr><td>${addressComponents[component]}</td><td>${component}</td></tr>`
         $("#address-parts").append(row);
      }
   }

   showResults();
}

function writeError(message) {
   // Write Error Message text
   $("#error-message").text(message);

   showError();
}



function showResults() {
   showOrHideById("error", false)
   showOrHideById("address-results", true)
}

function showError() {
   showOrHideById("address-results", false)
   showOrHideById("error", true)
}

function showOrHideById(id, show) {
   var setting = show ? '' : 'none';
   $(`#${id}`).css("display", setting);
}
