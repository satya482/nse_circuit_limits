const inputCsv = document.getElementById("inputCsv");
const outputText = document.getElementById("outputText");
const fileInput = document.getElementById("fileInput");
const dateColumn = document.getElementById("dateColumn");
const deliveryColumn = document.getElementById("deliveryColumn");
const statusEl = document.getElementById("status");
const rowCountEl = document.getElementById("rowCount");
const rangeTextEl = document.getElementById("rangeText");
const charCountEl = document.getElementById("charCount");

const sample = `Date,% Dly Qt to Traded Qty
07-Jul-2026,22.02
06-Jul-2026,30.82
03-Jul-2026,41.55
30-Apr-2026,51.33
01-Apr-2026,48.10
30-Mar-2026,62.42
02-Mar-2026,39.77`;

function setStatus(msg, isError = false) {
  statusEl.textContent = msg;
  statusEl.className = isError ? "status error" : "status";
}

function parseCsv(text) {
  const rows = [];
  let row = [];
  let cell = "";
  let quoted = false;

  for (let i = 0; i < text.length; i++) {
    const ch = text[i];
    const next = text[i + 1];

    if (ch === '"' && quoted && next === '"') {
      cell += '"';
      i++;
    } else if (ch === '"') {
      quoted = !quoted;
    } else if (ch === "," && !quoted) {
      row.push(cell);
      cell = "";
    } else if ((ch === "\n" || ch === "\r") && !quoted) {
      if (ch === "\r" && next === "\n") i++;
      row.push(cell);
      if (row.some(v => v.trim() !== "")) rows.push(row);
      row = [];
      cell = "";
    } else {
      cell += ch;
    }
  }

  row.push(cell);
  if (row.some(v => v.trim() !== "")) rows.push(row);

  return rows;
}

function normalizeHeader(h) {
  return String(h || "")
    .toLowerCase()
    .replace(/["'%._\-()]/g, " ")
    .replace(/\s+/g, " ")
    .trim();
}

function detectColumns(headers) {
  const norm = headers.map(normalizeHeader);

  let dateIdx = norm.findIndex(h =>
    h === "date" ||
    h === "date1" ||
    h.includes("date")
  );

  let delIdx = norm.findIndex(h =>
    h.includes("dly qt to traded qty") ||
    h.includes("delivery") ||
    (h.includes("dly") && h.includes("traded")) ||
    h.includes("deliv")
  );

  // Compact 2-column fallback.
  if (dateIdx < 0 && headers.length >= 1) dateIdx = 0;
  if (delIdx < 0 && headers.length >= 2) delIdx = headers.length - 1;

  return { dateIdx, delIdx };
}

function rebuildColumnDropdowns() {
  const rows = parseCsv(inputCsv.value);
  const headers = rows.length ? rows[0] : [];

  dateColumn.innerHTML = "";
  deliveryColumn.innerHTML = "";

  if (!headers.length) {
    const opt = new Option("No columns detected", "-1");
    dateColumn.add(opt.cloneNode(true));
    deliveryColumn.add(opt);
    return;
  }

  headers.forEach((h, idx) => {
    const label = `${idx}: ${String(h || "").trim() || "(blank)"}`;
    dateColumn.add(new Option(label, String(idx)));
    deliveryColumn.add(new Option(label, String(idx)));
  });

  const detected = detectColumns(headers);
  dateColumn.value = String(detected.dateIdx);
  deliveryColumn.value = String(detected.delIdx);
}

function parseNseDateToKey(value) {
  const s = String(value || "").trim().replace(/^"|"$/g, "");
  if (!s) return null;

  // Already numeric YYYYMMDD.
  if (/^\d{8}$/.test(s)) return s;

  // ISO YYYY-MM-DD.
  let m = s.match(/^(\d{4})-(\d{2})-(\d{2})$/);
  if (m) return `${m[1]}${m[2]}${m[3]}`;

  // NSE DD-Mon-YYYY.
  m = s.match(/^(\d{1,2})-([A-Za-z]{3})-(\d{4})$/);
  if (m) {
    const months = {
      jan: "01", feb: "02", mar: "03", apr: "04", may: "05", jun: "06",
      jul: "07", aug: "08", sep: "09", oct: "10", nov: "11", dec: "12"
    };
    const dd = m[1].padStart(2, "0");
    const mm = months[m[2].toLowerCase()];
    const yy = m[3];
    if (mm) return `${yy}${mm}${dd}`;
  }

  // JS Date fallback for rare files.
  const dt = new Date(s);
  if (!Number.isNaN(dt.getTime())) {
    const yy = dt.getFullYear();
    const mm = String(dt.getMonth() + 1).padStart(2, "0");
    const dd = String(dt.getDate()).padStart(2, "0");
    return `${yy}${mm}${dd}`;
  }

  return null;
}

function cleanNumber(value) {
  const s = String(value || "")
    .trim()
    .replace(/^"|"$/g, "")
    .replace(/,/g, "");

  const n = Number(s);
  return Number.isFinite(n) ? n : null;
}

function keyToIso(key) {
  return `${key.slice(0, 4)}-${key.slice(4, 6)}-${key.slice(6, 8)}`;
}

function convert() {
  const rows = parseCsv(inputCsv.value);
  if (rows.length < 2) {
    setStatus("Paste or upload CSV first.", true);
    return;
  }

  const dIdx = Number(dateColumn.value);
  const vIdx = Number(deliveryColumn.value);

  if (dIdx < 0 || vIdx < 0) {
    setStatus("Could not detect columns. Select them manually.", true);
    return;
  }

  const out = [["DateKey", "Delivery%"]];
  let skipped = 0;

  for (let i = 1; i < rows.length; i++) {
    const r = rows[i];
    const key = parseNseDateToKey(r[dIdx]);
    const val = cleanNumber(r[vIdx]);

    if (!key || val === null) {
      skipped++;
      continue;
    }

    out.push([key, String(Number(val.toFixed(2)))]);
  }

  const text = out.map(r => r.join(",")).join("\n");
  outputText.value = text;

  const dataRows = out.slice(1);
  rowCountEl.textContent = String(dataRows.length);
  charCountEl.textContent = String(text.length);

  if (dataRows.length) {
    const keys = dataRows.map(r => r[0]).sort();
    rangeTextEl.textContent = `${keyToIso(keys[0])} → ${keyToIso(keys[keys.length - 1])}`;
  } else {
    rangeTextEl.textContent = "—";
  }

  const msg = skipped
    ? `Converted ${dataRows.length} rows. Skipped ${skipped} invalid rows.`
    : `Converted ${dataRows.length} rows.`;

  setStatus(msg, skipped > 0);
}

async function copyOutput() {
  if (!outputText.value.trim()) {
    setStatus("Nothing to copy. Convert first.", true);
    return;
  }

  try {
    await navigator.clipboard.writeText(outputText.value);
    setStatus("Copied output to clipboard.");
  } catch {
    outputText.select();
    document.execCommand("copy");
    setStatus("Copied output to clipboard.");
  }
}

function downloadOutput() {
  if (!outputText.value.trim()) {
    setStatus("Nothing to download. Convert first.", true);
    return;
  }

  const blob = new Blob([outputText.value], { type: "text/plain;charset=utf-8" });
  const a = document.createElement("a");
  a.href = URL.createObjectURL(blob);
  a.download = "nse-delivery-tradingview.txt";
  document.body.appendChild(a);
  a.click();
  a.remove();
  URL.revokeObjectURL(a.href);
}

fileInput.addEventListener("change", async () => {
  const file = fileInput.files?.[0];
  if (!file) return;

  const text = await file.text();
  inputCsv.value = text;
  rebuildColumnDropdowns();
  setStatus(`Loaded ${file.name}.`);
});

inputCsv.addEventListener("input", rebuildColumnDropdowns);

document.getElementById("sampleBtn").addEventListener("click", () => {
  inputCsv.value = sample;
  rebuildColumnDropdowns();
  convert();
});

document.getElementById("clearBtn").addEventListener("click", () => {
  inputCsv.value = "";
  outputText.value = "";
  rowCountEl.textContent = "0";
  rangeTextEl.textContent = "—";
  charCountEl.textContent = "0";
  rebuildColumnDropdowns();
  setStatus("Cleared.");
});

document.getElementById("convertBtn").addEventListener("click", convert);
document.getElementById("copyBtn").addEventListener("click", copyOutput);
document.getElementById("downloadBtn").addEventListener("click", downloadOutput);

rebuildColumnDropdowns();
