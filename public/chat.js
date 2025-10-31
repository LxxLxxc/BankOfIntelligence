function sendPrompt() {
  const prompt = document.getElementById("userPrompt").value;
  const responseBox = document.getElementById("responseBox");

  if (!prompt.trim()) {
    responseBox.innerHTML = "<p>يرجى كتابة فكرة أولاً.</p>";
    return;
  }

  fetch("/api/intelli_agent", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ message: prompt })
  })
  .then(res => res.json())
  .then(data => {
    responseBox.innerHTML = `<p><strong>الرد:</strong> ${data.response}</p>`;
  })
  .catch(err => {
    responseBox.innerHTML = `<p style="color:red;">حدث خطأ: ${err.message}</p>`;
  });
}
