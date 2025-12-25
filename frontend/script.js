document.getElementById("evaluateBtn").addEventListener("click", evaluate);

async function evaluate() {
  const fileInput = document.getElementById("resumeFile");
  const role = document.getElementById("role").value;
  const resultDiv = document.getElementById("result");

  if (fileInput.files.length === 0) {
    alert("Please upload a resume");
    return;
  }

  resultDiv.style.display = "block";
  resultDiv.innerHTML = "🔍 Analyzing resume using Gemini AI...";

  const formData = new FormData();
  formData.append("resume", fileInput.files[0]);
  formData.append("role", role);

  try {
    fetch("http://127.0.0.1:8000/evaluate", {
      method: "POST",
      body: formData
    })
      .then(response => response.json())
      .then(data => {
        // ✅ STORE RESULT
        localStorage.setItem("result", data.result);

        // ✅ REDIRECT TO DASHBOARD
        window.location.href = "dashboard.html";
      })
      .catch(error => {
        resultDiv.innerHTML = "❌ Error analyzing resume.";
        console.error(error);
      });

  } catch (error) {
    resultDiv.innerHTML = "❌ Error analyzing resume.";
    console.error(error);
  }
}
