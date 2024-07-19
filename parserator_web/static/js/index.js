/* TODO: Flesh this out to connect the form to the API and render results
   in the #address-results div. */
const form = document.querySelector('.form')

form.addEventListener('submit', async (e) => {
  e.preventDefault()
  const input = document.querySelector('.form-control').value
  if (input === "") {
    displayAddressResults('blankInput')
    return
  } 
  try {
    displayAddressResults('loading')
		  const response = await fetch(`/api/parse/?address=${input}`)

    if(!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`)
    }
    const data = await response.json()
    displayAddressResults('success', data)
  }
  catch (error) {
    console.error('There was a problem with the fetch operation')
    displayAddressResults('error', error.message)
  }
})

const displayAddressResults = (status, data = null) => {
  const addressResults = document.querySelector('#address-results')
  addressResults.style.display = 'block'
  switch(status) {
  case 'loading':
    addressResults.innerHTML = '<p>Loading...</p>';
    break
  case 'blankInput':
    addressResults.innerHTML = `
        <h4>Parsing results</h4>
        <p>Search input cannot be blank.</p>
        `
    break
  case 'success':
    let tableRows = ''
    for (const [key, value] of Object.entries(data.address_components)) {
      tableRows += `
          <tr>
            <td>${value}</td>
            <td>${key}</td>
          </tr>
          `
    }
    addressResults.innerHTML = `
          <h4>Parsing results</h4>
          <p>Address type: <strong><span id="parse-type">${data.address_type}</span></strong></p>
          <table class="table table-bordered">
            <thead>
              <tr>
                <th>Address part</th>
                <th>Tag</th>
              </tr>
            </thead>
            <tbody>
              ${tableRows}
            </tbody>
          </table>
      `
    break
  case 'error':
    addressResults.innerHTML = `
        <h4>Parsing results</h4>
        <strong><p>${data}</p></strong>
        <p>Check your address and try again.</p>
      `
    break
  }
}