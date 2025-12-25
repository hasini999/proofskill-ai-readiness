const raw = localStorage.getItem("result");

if (raw) {
  const lines = raw.split("\n").filter(l => l.trim());

  document.getElementById("score").innerText =
    lines.find(l => l.includes("Score"))?.match(/\d+/)?.[0] + " / 100";

  fillList("strengths", lines, "Strengths");
  fillList("gaps", lines, "Skill Gaps");
  fillList("actions", lines, "Next Steps");
}

function fillList(id, lines, keyword) {
  const ul = document.getElementById(id);
  let start = lines.findIndex(l => l.includes(keyword));
  if (start === -1) return;

  for (let i = start + 1; i < lines.length && !lines[i].includes(":"); i++) {
    const li = document.createElement("li");
    li.innerText = lines[i].replace("-", "").trim();
    ul.appendChild(li);
  }
}

function downloadPDF() {
  window.print();
}
