document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('prediction-form');
    const resultDiv = document.getElementById('prediction-result');

    form.addEventListener('submit', async (event) => {
      event.preventDefault();

      const formData = new FormData(form);
      const data = Object.fromEntries(formData.entries());

      try {
        const response = await fetch('/predict', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(data),
        });

        if (response.ok) {
          const result = await response.json();
          resultDiv.textContent = `The Prediction is ${result.prediction}`;
        } else {
          resultDiv.textContent = 'An error occurred while making the prediction.';
        }
      } catch (error) {
        resultDiv.textContent = 'An error occurred while connecting to the server.';
      }
    });
  });
