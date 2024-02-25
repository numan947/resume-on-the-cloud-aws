document.addEventListener("DOMContentLoaded", function () {
	// Get a reference to the image element
	var imageElement = document.getElementById("profileViewButtonLoadingImage");
	var spanElement = document.getElementById("profileViewCount");

	// Fetch data from the API endpoint
	if (imageElement && spanElement) {
		fetch('https://cmp0ltkns5.execute-api.us-east-2.amazonaws.com/Prod/post',
			{
				method: 'POST',
				headers: {
					'Content-Type': 'application/json'
				}
			}

		)
			.then(response => {
				// Check if the response is successful
				if (!response.ok) {
					throw new Error("Network response was not ok");
				}
				// Parse the JSON response
				return response.json();
			})
			.then(data => {
				// Print the retrieved data to the console
				console.log(data);

				// Hide the image after fetch complete
				update(data);
			})
			.catch(error => {
				// Handle any errors that occurred during the fetch
				console.error("Error fetching data:", error);
			});
	}

	// Function to hide the image
	function update(data) {
		if (imageElement && spanElement) {
			imageElement.style.display = "none";
			spanElement.textContent = data['count'];
		} else {
			console.error("Image element not found!");
		}
	}
});


