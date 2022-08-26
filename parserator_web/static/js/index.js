/* TODO: Flesh this out to connect the form to the API and render results
   in the #address-results div. */
const submitButton = document.querySelector(".btn")
const addressInput = document.querySelector(".form-control")
const addressResults = document.querySelector(".address-results")


//function to take in user input and send to api

const sendAddress = (userInput) => {
   return fetch(`http://localhost:8000/${userInput}`)
      .then(response => {
         if (!response.ok) {
            throw Error(response.statusText)
         } else {
            return response.json()

         }
      })
      .catch(err => displayError(err))
}


const displayError = () => {
   //add error area in HTML?
}


const displayResults = (e) => {
   e.preventDefault()
   if (Event.target == submitButton) {
      sendAddress(addressInput.value)
      addressResults.style.display = "block"
   }
}

submitButton.addEventListener("click", displayResults)


