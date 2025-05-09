let namespace = null;

function appendMessage(sender, text) {
  const box = document.getElementById("chat-box");
  const msgDiv = document.createElement("div");

  msgDiv.className = `message-${sender} px-4`;
msgDiv.innerHTML = `
  <div class="container mx-auto max-w-4xl">
    <div class="flex ${sender === 'user' ? 'flex-row' : 'flex-row-reverse'} items-start gap-4">
      <div class="flex-shrink-0">
        <img src="${sender === 'user' 
          ? 'https://avatars.githubusercontent.com/u/1?v=4'
          : 'https://cdn-icons-png.flaticon.com/512/4712/4712106.png'}" 
          class="h-8 w-8 rounded-full" />
      </div>
      <div class="flex-1">
        <div class="inline-block px-4 py-2 rounded-xl text-white max-w-[90%] break-words text-left
          ${sender === 'user' ? 'bg-[#3c3d4a]' : 'bg-[#565869]'}">
          ${text}
        </div>
      </div>
    </div>
  </div>`;

  box.appendChild(msgDiv);
  box.scrollTop = box.scrollHeight;
}

async function uploadPDF() {
  const file = document.getElementById("pdfFile").files[0];
  const btn = document.getElementById("uploadBtn");
  const spinner = document.getElementById("uploadSpinner");
  const btnText = document.getElementById("uploadBtnText");

  if (!file) return Swal.fire("No file selected", "", "warning");

  // Start loading state
  btn.disabled = true;
  spinner.classList.remove("hidden");
  btnText.textContent = "Uploading";

  try {
    const formData = new FormData();
    formData.append("file", file);

    const res = await fetch("/api/v1/upload", {
      method: "POST",
      body: formData,
    });

    const data = await res.json();
    if (res.ok) {
      namespace = data.namespace;
      Swal.fire("Upload successful", "", "success");
      btnText.textContent = "Uploaded";
    } else {
      throw new Error(data.detail || "Upload failed");
    }
  } catch (err) {
    Swal.fire("Upload failed", err.message, "error");
    btn.disabled = false;
    btnText.textContent = "Upload";
  } finally {
    spinner.classList.add("hidden");
  }
}

async function askQuestion() {
  const question = document.getElementById("question").value;
  if (!question) return;
  if (!namespace) return Swal.fire("Upload a PDF first", "", "info");

  appendMessage("user", question);
  document.getElementById("question").value = "";
  appendMessage("bot", "<span class='loading-dots'></span>");

  try {
    const res = await fetch("/api/v1/query", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ question, namespace }),
    });

    const data = await res.json();
    const chatBox = document.getElementById("chat-box");
    chatBox.removeChild(chatBox.lastChild); // remove loading animation

    if (res.ok) {
      appendMessage("bot", data.response || "(No answer)");
    } else {
      appendMessage("bot", "Error: Could not get response");
    }
  } catch {
    appendMessage("bot", "Error: Something went wrong");
  }
}
