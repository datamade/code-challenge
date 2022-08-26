/* Connects the form to the API and render results
   in the #address-results div. */

$('.form').on('submit', function (event) {
   event.preventDefault();
   submitAddress();
});

function getAddress() {
   var address = $("#address").val();
   return address.trim().replaceAll(" ", "+");
}

function submitAddress() {
   var url = "api/parse?address=" + getAddress();
   try {
      fetch(url)
         .then((res) => handleResponse(res));
   } catch (error) {
      writeError("Something went wrong, please try again.");
   }
}

function handleResponse(response) {
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
   writeTextById("parse-type", addressType);
   writeAddressComponents(addressComponents);
   showResults();
}

function writeAddressComponents(addressComponents) {
   $("#address-parts").empty();
   for (var component in addressComponents) {
      if (Object.prototype.hasOwnProperty.call(addressComponents, component)) {
         var row = `<tr><td>${addressComponents[component]}</td><td>${component}</td></tr>`
         $("#address-parts").append(row);
      }
   }
}

function writeError(message) {
   writeTextById("error-message", message);
   showError();
}

function showResults() {
   hide("error")
   show("address-results")
}

function showError() {
   hide("address-results")
   show("error")
}

function show(id) {
   showOrHideById(id, true)
}

function hide(id) {
   showOrHideById(id, false)
}

function showOrHideById(id, show) {
   var setting = show ? '' : 'none';
   $(`#${id}`).css("display", setting);
}


function writeTextById(id, text) {
   $(`#${id}`).text(text);
}
