document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("shorten-form");
    const resultDiv = document.getElementById("result");
    const shortUrlInput = document.getElementById("short-url");
    const copyBtn = document.getElementById("copy-btn");
    const errorMessage = document.getElementById("error-message");

    form.addEventListener("submit", async function (event) {
        event.preventDefault(); // Prevent page reload

        const longUrl = document.getElementById("long-url").value;
        const customAlias = document.getElementById("custom-alias").value;

        try {
            const response = await fetch("/shorten", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ url: longUrl, alias: customAlias })
            });

            const data = await response.json();

            if (response.ok) {
                shortUrlInput.value = data.short_url;
                resultDiv.classList.remove("hidden");
                errorMessage.classList.add("hidden");
            } else {
                errorMessage.textContent = data.error;
                errorMessage.classList.remove("hidden");
            }
        } catch (error) {
            errorMessage.textContent = "An error occurred. Please try again.";
            errorMessage.classList.remove("hidden");
        }
    });

    copyBtn.addEventListener("click", function () {
        shortUrlInput.select();
        document.execCommand("copy");
        copyBtn.textContent = "Copied!";
        setTimeout(() => (copyBtn.textContent = "Copy"), 2000);
    });
});
