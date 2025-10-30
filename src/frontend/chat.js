// chat.js – واجهة تنفيذ الأوامر من المستخدم إلى الذكاء الاصطناعي

async function sendPrompt() {
  const prompt = document.getElementById("userPrompt").value.trim();
  const responseBox = document.getElementById("responseBox");

  if (!prompt) {
    responseBox.innerHTML = "<p>يرجى كتابة فكرة لتنفيذها.</p>";
    return;
  }

  responseBox.innerHTML = "<p>جاري التنفيذ...</p>";

  try {
    const response = await fetch("../src/ai/ai_agent.py", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ prompt: prompt })
    });

    const result = await response.text();
    responseBox.innerHTML = `<pre>${result}</pre>`;
  } catch (error) {
    responseBox.innerHTML = `<p>حدث خطأ أثناء التنفيذ: ${error.message}</p>`;
  }
}
