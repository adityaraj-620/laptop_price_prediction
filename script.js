
document.getElementById("predictForm").addEventListener("submit", async function (e) {
    e.preventDefault();

    const formData = {
        brand: document.getElementById("brand").value,
        processor: document.getElementById("processor").value,
        ram: parseInt(document.getElementById("ram").value),
        storage: parseInt(document.getElementById("storage").value),
        gpu: document.getElementById("gpu").value,
        os: document.getElementById("os").value
    };

    const response = await fetch("http://localhost:5000/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(formData)
    });

    const result = await response.json();
    document.getElementById("result").innerText = "Predicted Price: ₹" + result.predicted_price;
});
