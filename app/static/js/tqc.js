let questions = [];
let activeId = null;
let selectedPrefixes = new Set(); // 沒勾選 => 不顯示任何題目

// ---------- helpers ----------
function matchPrefix(qid){
  if (selectedPrefixes.size === 0) return false; // ✅ 沒勾選：不顯示任何題
  const s = String(qid);
  return selectedPrefixes.has(Number(s[0]));
}

function initPrefixFilter(){
  const grid = document.getElementById("catGrid");
  grid.innerHTML = "";

  for(let n=1; n<=9; n++){
    const label = document.createElement("label");
    label.className = "catItem";
    label.innerHTML = `
      <input type="checkbox" value="${n}">
      <span class="catBadge">${n}</span>
    `;

    const cb = label.querySelector("input");
    cb.addEventListener("change", () => {
      const v = Number(cb.value);
      if (cb.checked) selectedPrefixes.add(v);
      else selectedPrefixes.delete(v);

      renderList(document.getElementById("search").value);
      ensureActiveVisible();
    });

    grid.appendChild(label);
  }
}

function renderList(filterText=""){
  const list = document.getElementById("list");
  const hint = document.getElementById("listHint");
  list.innerHTML = "";

  // ✅ 沒勾選：顯示提示
  if (selectedPrefixes.size === 0){
    if (hint) hint.style.display = "block";
    return;
  }else{
    if (hint) hint.style.display = "none";
  }

  const ft = filterText.trim().toLowerCase();

  questions
    .filter(q => {
      if (!matchPrefix(q.id)) return false;
      if (!ft) return true;
      return (String(q.id) + " " + q.title).toLowerCase().includes(ft);
    })
    .forEach(q => {
      const div = document.createElement("div");
      div.className = "qitem" + (q.id === activeId ? " active" : "");
      div.innerHTML = `<div class="qtitle">TQC ${q.id}－${q.title}</div>`;
      div.onclick = () => loadQuestion(q.id);
      list.appendChild(div);
    });
}

function ensureActiveVisible(){
  // ✅ 沒勾選：右側清空提示
  if (selectedPrefixes.size === 0){
    activeId = null;
    document.getElementById("rightTitle").textContent = "王大名請先勾選類別";
    document.getElementById("rightHint").textContent = "勾選 1～9 類後才會顯示對應題目清單。";
    document.getElementById("formArea").innerHTML = "";
    document.getElementById("resultArea").innerHTML = "";
    const codeBox = document.getElementById("codeBox");
    if (codeBox) codeBox.style.display = "none";

    const answerBox = document.getElementById("answerBox");
    if (answerBox) answerBox.style.display = "none";

    return;
  }

  const ft = document.getElementById("search").value.trim().toLowerCase();

  const visible = questions.filter(q => {
    if (!matchPrefix(q.id)) return false;
    if (!ft) return true;
    return (String(q.id) + " " + q.title).toLowerCase().includes(ft);
  });

  // ✅ 有勾選但沒有符合：顯示空狀態
  if (visible.length === 0){
    activeId = null;
    document.getElementById("rightTitle").textContent = "（沒有符合篩選的題目）";
    document.getElementById("rightHint").textContent = "請調整搜尋或勾選類別。";
    document.getElementById("formArea").innerHTML = "";
    document.getElementById("resultArea").innerHTML = "";
    const codeBox = document.getElementById("codeBox");
    if (codeBox) codeBox.style.display = "none";

    const answerBox = document.getElementById("answerBox");
    if (answerBox) answerBox.style.display = "none";

    return;
  }

  // ✅ 你要求：勾選後「不要自動載入第一題」，所以這裡只提示，不自動 load
  if (!activeId || !visible.some(q => q.id === activeId)){
    activeId = null;
    document.getElementById("rightTitle").textContent = "請從左邊選擇題目";
    document.getElementById("rightHint").textContent = "已依類別篩選完成，請點選題目。";
    document.getElementById("formArea").innerHTML = "";
    document.getElementById("resultArea").innerHTML = "";
    const codeBox = document.getElementById("codeBox");
    if (codeBox) codeBox.style.display = "none";

    const answerBox = document.getElementById("answerBox");
    if (answerBox) answerBox.style.display = "none";

  }
}

function safeMeta(meta, name){
  return (meta && meta[name]) ? meta[name] : {};
}

function buildForm(q){
  const meta = q.input_meta || {};
  const inputs = q.inputs || [];

  const formArea = document.getElementById("formArea");
  const resultArea = document.getElementById("resultArea");
  resultArea.innerHTML = "";

  let html = `<div class="grid">`;
  inputs.forEach((name, idx) => {
    const m = safeMeta(meta, name);
    const label = m.label || name;
    const unit = m.unit ? ` <span class="unit">(${m.unit})</span>` : "";
    const ph = m.placeholder || ("請輸入 " + name);

    const isFull = (inputs.length % 2 === 1) && (idx === inputs.length - 1);
    html += `
      <div class="field ${isFull ? "full" : ""}">
        <label>${label}${unit}</label>
        <input id="in_${name}" placeholder="${ph}">
      </div>
    `;
  });

  html += `</div>
    <div class="row">
      <button class="btn" id="runBtn" type="button">執行</button>
      <span id="callHint" class="muted"></span>
    </div>
  `;

  if (q.output_hint){
    html += `<p class="muted" style="margin-top:10px">輸出提示：${q.output_hint}</p>`;
  }

  formArea.innerHTML = html;
  formArea.dataset.qid = q.id;
  formArea.dataset.inputs = JSON.stringify(inputs);

  // ✅ 綁定按鈕事件（避免 inline onclick）
  document.getElementById("runBtn").addEventListener("click", runTQC);
}

function renderResult(d){
  const resultArea = document.getElementById("resultArea");
  resultArea.innerHTML = "";

  if (!d || d.ok === false){
    const msg = (d && d.error) ? d.error : "Unknown error";
    resultArea.innerHTML = `<div class="err">錯誤：${msg}</div>`;
    return;
  }

  if (typeof d.output === "string"){
    resultArea.innerHTML = `<div class="ok">${d.output}</div>`;
    return;
  }

  const ignore = new Set(["ok","qid"]);
  const keys = Object.keys(d).filter(k => !ignore.has(k));

  if (keys.length === 0){
    resultArea.innerHTML = `<div class="ok">（沒有結果欄位）</div>`;
    return;
  }

  let rows = "";
  keys.forEach(k => {
    rows += `<tr><td>${k}</td><td>${d[k]}</td></tr>`;
  });

  resultArea.innerHTML = `
    <table>
      <thead><tr><th>欄位</th><th>值</th></tr></thead>
      <tbody>${rows}</tbody>
    </table>
  `;
}

// ---------- API calls ----------
async function loadQuestion(qid){
  activeId = qid;
  renderList(document.getElementById("search").value);

  document.getElementById("rightTitle").textContent = `載入中…`;
  document.getElementById("rightHint").textContent = `讀取 /api/question/${qid}`;

  const r = await fetch(`/api/question/${qid}`);
  const q = await r.json();

  if(!q.ok){
    document.getElementById("rightTitle").textContent = `TQC ${qid}`;
    document.getElementById("rightHint").textContent = `錯誤：${q.error}`;
    document.getElementById("formArea").innerHTML = "";
    document.getElementById("resultArea").innerHTML = "";
    const codeBox = document.getElementById("codeBox");
    if (codeBox) codeBox.style.display = "none";

    const answerBox = document.getElementById("answerBox");
    if (answerBox) answerBox.style.display = "none";

    return;
  }

  document.getElementById("rightTitle").textContent = `TQC ${q.id}－${q.title}`;
  document.getElementById("rightHint").textContent = `按「執行」呼叫 /api/tqc/${q.id}（不換頁）`;

  buildForm(q);
  loadSourceCode(q.id);
  loadAnswerCode(q.id);

}

async function runTQC(){
  const formArea = document.getElementById("formArea");
  const qid = formArea.dataset.qid;
  const inputs = JSON.parse(formArea.dataset.inputs || "[]");

  const payload = {};
  inputs.forEach(name => {
    payload[name] = document.getElementById("in_" + name).value;
  });

  document.getElementById("callHint").textContent = "呼叫中…";

  try{
    const r = await fetch(`/api/tqc/${qid}`, {
      method:"POST",
      headers: {"Content-Type":"application/json"},
      body: JSON.stringify(payload)
    });
    const d = await r.json();
    document.getElementById("callHint").textContent = "";
    renderResult(d);
  }catch(e){
    document.getElementById("callHint").textContent = "";
    renderResult({ok:false, error:"網路或伺服器錯誤：" + e});
  }
}

async function loadSourceCode(qid){
  const box = document.getElementById("codeBox");
  const title = document.getElementById("codeTitle");
  const codeEl = document.getElementById("codeContent");
  const toggleBtn = document.getElementById("toggleBtn");

  title.textContent = `q${qid}.py`;
  codeEl.textContent = "載入程式碼中…";
  box.style.display = "block";
  box.classList.add("collapsed");        // ✅ 預設收合
  if (toggleBtn) toggleBtn.textContent = "展開程式碼";

  try{
    const r = await fetch(`/api/source/${qid}`);
    if(!r.ok){
      const msg = await r.text();
      codeEl.textContent = `（無法載入：${r.status}）\n${msg}`;
      return;
    }
    const code = await r.text();
    codeEl.textContent = code;
  }catch(e){
    codeEl.textContent = `（網路或伺服器錯誤）\n${e}`;
  }
}

async function loadAnswerCode(qid){
  const box = document.getElementById("answerBox");
  const title = document.getElementById("answerTitle");
  const codeEl = document.getElementById("answerContent");
  const toggleBtn = document.getElementById("answerToggleBtn");


  title.textContent = `PYA${qid}.py`;
  codeEl.textContent = "載入題庫解答中…";
  box.style.display = "block";
  box.classList.add("collapsed");      // 預設收合
  if (toggleBtn) toggleBtn.textContent = "證照題庫解答";


  try{
    const r = await fetch(`/api/answer/${qid}`);
    if(!r.ok){
      const msg = await r.text();
      codeEl.textContent = `（無法載入：${r.status}）\n${msg}`;
      return;
    }


    const code = await r.text();
    codeEl.textContent = code;
  }catch(e){
    codeEl.textContent = `（網路或伺服器錯誤）\n${e}`;
  }
}


// ---------- codebox buttons ----------
function toggleCode(){
  const box = document.getElementById("codeBox");
  const btn = document.getElementById("toggleBtn");
  const collapsed = box.classList.toggle("collapsed");
  btn.textContent = collapsed ? "展開程式碼" : "收合程式碼";
}

function toggleAnswer(){
  const box = document.getElementById("answerBox");
  const btn = document.getElementById("answerToggleBtn");
  const collapsed = box.classList.toggle("collapsed");
  btn.textContent = collapsed ? "證照題庫解答" : "收合解答";
}


function copyCode(){
  const code = document.getElementById("codeContent").textContent || "";
  navigator.clipboard.writeText(code).then(()=>{
    const btn = document.getElementById("copyBtn");
    const old = btn.textContent;
    btn.textContent = "已複製";
    setTimeout(()=> btn.textContent = old, 800);
  });
}

function copyAnswer(){
  const code = document.getElementById("answerContent").textContent || "";
  navigator.clipboard.writeText(code).then(()=>{
    const btn = document.getElementById("answerCopyBtn");
    const old = btn.textContent;
    btn.textContent = "已複製";
    setTimeout(()=> btn.textContent = old, 800);
  });
}


// ---------- init ----------
document.addEventListener("DOMContentLoaded", () => {
  initPrefixFilter();

  // 綁定外部按鈕事件
  document.getElementById("toggleBtn").addEventListener("click", toggleCode);
  document.getElementById("copyBtn").addEventListener("click", copyCode);

  document.getElementById("answerToggleBtn").addEventListener("click", toggleAnswer);
  document.getElementById("answerCopyBtn").addEventListener("click", copyAnswer);

  fetch("/api/questions")
    .then(r => r.json())
    .then(list => {
      questions = list;

      // ✅ 一開始沒勾選：清單空、右側提示
      renderList("");
      ensureActiveVisible();
    });

  document.getElementById("search").addEventListener("input", (e)=>{
    renderList(e.target.value);
    ensureActiveVisible();
  });
});
