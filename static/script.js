function analyzeReviews() {
    const url = document.getElementById("url").value;
    const resultDiv = document.getElementById("result");
    const loadingDiv = document.getElementById("loading");

    if (!url) {
        resultDiv.innerHTML = "<p style='color: red;'>⚠ Please enter a valid product URL.</p>";
        return;
    }

    resultDiv.innerHTML = "";
    loadingDiv.style.display = "block";

    // fetch("/analyze", {
    //     method: "POST",
    //     headers: { "Content-Type": "application/json" },
    //     body: JSON.stringify({ url: url })
    // })
    fetch("https://fake-review-detection-l3t8.onrender.com/analyze", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ url: url })
    })
    .then(response => response.json())
    .then(data => {
        loadingDiv.style.display = "none";
        if (data.error) {
            resultDiv.innerHTML = `<p style='color: red;'>⚠ ${data.error}</p>`;
        } else {
            let html = "<h2>Results</h2><div class='review-container'>";
            data.forEach(review => {
                const predictionClass = review.Prediction === "Real (Original)" ? "real" : "fake";
                html += `
                    <div class="review-card">
                        <p class="review-text"><strong>Review:</strong> ${review.Review}</p>
                        <p class="review-rating"><strong>Rating:</strong> ⭐ ${review.Rating}</p>
                        <p class="review-prediction ${predictionClass}">
                            <strong>Prediction:</strong> ${review.Prediction}
                        </p>
                    </div>
                `;
            });
            html += "</div>";
            resultDiv.innerHTML = html;
        }
    })
    .catch(error => {
        loadingDiv.style.display = "none";
        resultDiv.innerHTML = "<p style='color: red;'>⚠ Error processing request.</p>";
    });
}
