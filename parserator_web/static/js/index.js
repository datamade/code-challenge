const submitButton = document.querySelector(".btn")
const addressInput = document.querySelector(".form-control")
const addressResults = document.querySelector(".address-results")
const resultsTable = document.querySelector(".results-table")

/** check if input is correct type before sending query
  * @param {string} input - user's address input
  * @returns {boolean} - is the input longer than 0
  * 
  * */    

const checkInput = input => {
   return input.length
}

const fetchAddress = async (userInput) => {
   const response = await fetch(`api/parse/?address=${userInput}`)
   const body = await response.json()
   return body
}



const displayError = () => {
   //add error area in HTML?
}

//if response is 200, map result array values and tags as <tr> <td>value</td> <tag>tag</tag> </tr>


const displayResults = (e) => {
   e.preventDefault()
   if (Event.target == submitButton) {
      sendAddress(addressInput.value)
         .then((result) => {

         })
   }
}

submitButton.addEventListener("click", displayResults)


